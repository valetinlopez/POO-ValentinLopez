const { Router } = require("express");
const productosController = require("../controllers/productos.controller");

const router = Router();

// ROUTES: solo define los endpoints y los conecta al controller correcto
// No tiene lógica, solo mapea URL + método HTTP → función del controller

router.get("/", productosController.getAll);
router.get("/:id", productosController.getById);
router.post("/", productosController.create);
router.put("/:id", productosController.update);
router.delete("/:id", productosController.remove);

module.exports = router;
