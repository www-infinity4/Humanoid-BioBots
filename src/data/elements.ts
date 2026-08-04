import { ElementInfo } from '../types/models';

export const ELEMENTS: Record<number, ElementInfo> = {
  15: { atomicNumber: 15, symbol: 'P', name: 'Phosphorus', category: 'power' },
  29: { atomicNumber: 29, symbol: 'Cu', name: 'Copper', category: 'wiring' },
  34: { atomicNumber: 34, symbol: 'Se', name: 'Selenium', category: 'sensors' },
  43: { atomicNumber: 43, symbol: 'Tc', name: 'Technetium', category: 'shielding' },
  51: { atomicNumber: 51, symbol: 'Sb', name: 'Antimony', category: 'structure' },
  92: { atomicNumber: 92, symbol: 'U', name: 'Uranium', category: 'power' }
};

export const PART_CATEGORIES = ['structure', 'power', 'sensors', 'wiring', 'shielding'] as const;
