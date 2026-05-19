const createHttpError = (message, status = 400) => {
  const error = new Error(message);
  error.status = status;
  return error;
};

const ensureNonEmptyString = (value, fieldName) => {
  if (typeof value !== "string" || value.trim() === "") {
    throw createHttpError(`El campo ${fieldName} es obligatorio`, 400);
  }

  return value.trim();
};

const ensurePositiveNumber = (value, fieldName) => {
  const parsed = Number(value);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw createHttpError(`El campo ${fieldName} debe ser mayor a cero`, 400);
  }

  return parsed;
};

const ensurePositiveInteger = (value, fieldName) => {
  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed <= 0) {
    throw createHttpError(`El campo ${fieldName} debe ser un entero mayor a cero`, 400);
  }

  return parsed;
};

const ensureNonNegativeInteger = (value, fieldName) => {
  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed < 0) {
    throw createHttpError(`El campo ${fieldName} no puede ser negativo`, 400);
  }

  return parsed;
};

const ensureOptionalBoolean = (value, fieldName) => {
  if (value === undefined) {
    return undefined;
  }

  if (typeof value !== "boolean") {
    throw createHttpError(`El campo ${fieldName} debe ser booleano`, 400);
  }

  return value;
};

const ensureValidEmail = (value) => {
  const email = ensureNonEmptyString(value, "email").toLowerCase();
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  if (!emailRegex.test(email)) {
    throw createHttpError("El email es inválido", 400);
  }

  return email;
};

const ensureId = (value, entityLabel = "id") => {
  const parsed = Number.parseInt(value, 10);
  if (!Number.isInteger(parsed) || parsed <= 0) {
    throw createHttpError(`El ${entityLabel} debe ser un entero mayor a cero`, 400);
  }

  return parsed;
};

module.exports = {
  createHttpError,
  ensureNonEmptyString,
  ensurePositiveNumber,
  ensurePositiveInteger,
  ensureNonNegativeInteger,
  ensureOptionalBoolean,
  ensureValidEmail,
  ensureId,
};
