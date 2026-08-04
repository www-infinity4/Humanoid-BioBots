import express from 'express';
import path from 'path';
import { PRESETS } from '../data/presets';
import { validateBuild } from '../core/validator';
import { saveBuild, listBuilds } from '../data/store';
import { BuildInput } from '../types/models';

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

app.get('/', (_req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.get('/health', (_req, res) => {
  res.json({ ok: true });
});

app.get('/presets', (_req, res) => {
  res.json(PRESETS);
});

app.post('/validate', (req, res) => {
  const input = req.body as BuildInput;
  const validation = validateBuild(input);
  res.json(validation);
});

app.post('/builds', (req, res) => {
  const input = req.body as BuildInput;
  const validation = validateBuild(input);
  const stored = saveBuild({
    id: `${Date.now()}`,
    input,
    validation,
    createdAt: new Date().toISOString()
  });
  res.status(201).json(stored);
});

app.get('/builds', (_req, res) => {
  res.json(listBuilds());
});

export default app;
