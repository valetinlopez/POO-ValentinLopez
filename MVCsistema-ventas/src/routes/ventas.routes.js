const { Router } = require("express");
const ventasController = require("../controllers/ventas.controller");

const router = Router();

router.get("/", ventasController.getAll);
router.get("/:id", ventasController.getById);
router.post("/", ventasController.create);
router.delete("/:id", ventasController.cancel); // cancelar una venta restaura el stock

module.exports = router;
