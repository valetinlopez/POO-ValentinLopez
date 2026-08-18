const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const compression = require('compression');

const config = require('./config');
const logger = require('./config/logger');
const routes = require('./routes');
const { errorHandler, notFoundHandler } = require('./middlewares/errorHandler');
const { apiLimiter } = require('./middlewares/rateLimiter');
const requestLogger = require('./middlewares/requestLogger');

const app = express();

app.use(helmet());
app.use(cors());
app.use(compression());
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

if (config.env !== 'test') {
  app.use(requestLogger);
}

app.use(apiLimiter);

app.use('/api/v1', routes);

app.use(notFoundHandler);
app.use(errorHandler);

const PORT = config.port;

const server = app.listen(PORT, () => {
  logger.info(`Server running on port ${PORT} in ${config.env} mode`);
});

const gracefulShutdown = (signal) => {
  logger.info(`${signal} received, shutting down gracefully`);
  server.close(() => {
    logger.info('Process terminated');
    process.exit(0);
  });
};

process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
process.on('SIGINT', () => gracefulShutdown('SIGINT'));

module.exports = app;
