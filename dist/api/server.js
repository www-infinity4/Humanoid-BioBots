"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const presets_1 = require("../data/presets");
const validator_1 = require("../core/validator");
const store_1 = require("../data/store");
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.get('/health', (_req, res) => {
    res.json({ ok: true });
});
app.get('/presets', (_req, res) => {
    res.json(presets_1.PRESETS);
});
app.post('/validate', (req, res) => {
    const input = req.body;
    const validation = (0, validator_1.validateBuild)(input);
    res.json(validation);
});
app.post('/builds', (req, res) => {
    const input = req.body;
    const validation = (0, validator_1.validateBuild)(input);
    const stored = (0, store_1.saveBuild)({
        id: `${Date.now()}`,
        input,
        validation,
        createdAt: new Date().toISOString()
    });
    res.status(201).json(stored);
});
app.get('/builds', (_req, res) => {
    res.json((0, store_1.listBuilds)());
});
exports.default = app;
//# sourceMappingURL=server.js.map