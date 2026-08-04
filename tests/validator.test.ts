import request from 'supertest';
import app from '../src/api/server';
import { validateBuild } from '../src/core/validator';

describe('safe validator', () => {
  it('accepts valid build', () => {
    const result = validateBuild({
      name: 'ok',
      parts: [
        { category: 'structure', atomicNumber: 51 },
        { category: 'power', atomicNumber: 15 },
        { category: 'shielding', atomicNumber: 43 }
      ],
      numbers: [51, 9, 15, 43],
      intents: ['education']
    });
    expect(result.status).toBe('valid build');
    expect(result.safety).toBe('green');
  });

  it('blocks forbidden pair', () => {
    const result = validateBuild({
      name: 'bad',
      parts: [
        { category: 'structure', atomicNumber: 51 },
        { category: 'sensors', atomicNumber: 34 },
        { category: 'power', atomicNumber: 15 },
        { category: 'shielding', atomicNumber: 43 }
      ],
      numbers: [51, 34, 15, 43],
      intents: ['education']
    });
    expect(result.status).toBe('rule broken');
  });

  it('applies 10 to 3 transform', () => {
    const result = validateBuild({
      name: 'transform',
      parts: [
        { category: 'power', atomicNumber: 15 },
        { category: 'shielding', atomicNumber: 43 }
      ],
      numbers: [10, 15, 43],
      intents: ['education']
    });
    expect(result.derivedNumbers).toContain(3);
  });

  it('red-lights blocked intent', () => {
    const result = validateBuild({
      name: 'unsafe',
      parts: [
        { category: 'power', atomicNumber: 15 },
        { category: 'shielding', atomicNumber: 43 }
      ],
      numbers: [15, 43],
      intents: ['weapon-like output']
    });
    expect(result.safety).toBe('red');
    expect(result.status).toBe('rule broken');
  });

  it('serves presets', async () => {
    const res = await request(app).get('/presets');
    expect(res.status).toBe(200);
    expect(res.body.single).toBeDefined();
  });
});
