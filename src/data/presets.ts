import { BuildInput } from '../types/models';

export const PRESETS: Record<string, BuildInput> = {
  single: {
    name: 'single',
    parts: [
      { category: 'structure', atomicNumber: 51 },
      { category: 'power', atomicNumber: 15 },
      { category: 'shielding', atomicNumber: 43 }
    ],
    numbers: [51, 9, 15, 43],
    intents: ['learning', 'health-safe']
  },
  couple: {
    name: 'couple',
    parts: [
      { category: 'structure', atomicNumber: 51 },
      { category: 'wiring', atomicNumber: 29 },
      { category: 'power', atomicNumber: 15 },
      { category: 'shielding', atomicNumber: 43 }
    ],
    numbers: [51, 92, 15, 43],
    intents: ['family support']
  },
  family: {
    name: 'family',
    parts: [
      { category: 'structure', atomicNumber: 51 },
      { category: 'sensors', atomicNumber: 34 },
      { category: 'power', atomicNumber: 15 },
      { category: 'shielding', atomicNumber: 43 }
    ],
    numbers: [15, 43, 10, 0],
    intents: ['education', 'care']
  }
};
