import { BuildInput, RuleCheck } from '../types/models';

const FORBIDDEN_PAIRS = new Set(['34-51', '51-34']);
const REQUIRED_PAIR = ['15-43', '43-15'];

export function normalizeNumber(num: number): number {
  if (num === 10) return 3;
  if (num === 0 || num === 9 || num === 92) return num;
  return num;
}

export function deriveNumbers(numbers: number[]): number[] {
  return numbers.map(normalizeNumber);
}

function hasPair(numbers: number[], pairs: string[]): boolean {
  const pairSet = new Set<string>();
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      pairSet.add(`${numbers[i]}-${numbers[j]}`);
      pairSet.add(`${numbers[j]}-${numbers[i]}`);
    }
  }
  return pairs.some((p) => pairSet.has(p));
}

export function runRuleChecks(input: BuildInput, derivedNumbers: number[]): RuleCheck[] {
  const checks: RuleCheck[] = [];

  checks.push({
    rule: 'forbidden-pair-51-34',
    passed: !hasPair(derivedNumbers, ['51-34', '34-51']),
    message: '51 with 34 is blocked by system rules.'
  });

  checks.push({
    rule: 'required-pair-15-43',
    passed: hasPair(derivedNumbers, REQUIRED_PAIR),
    message: 'Build should include 15 and 43 together.'
  });

  const has51 = derivedNumbers.includes(51);
  const hasCompanion = derivedNumbers.some((n) => [9, 0, 92, 3].includes(n));
  checks.push({
    rule: '51-companion-rule',
    passed: !has51 || hasCompanion,
    message: 'If 51 is present, include one of 9, 0, 92, or 10→3 transformed value.'
  });

  const hasMapped10 = input.numbers.includes(10) ? derivedNumbers.includes(3) : true;
  checks.push({
    rule: 'transform-10-to-3',
    passed: hasMapped10,
    message: '10 is transformed to 3.'
  });

  return checks;
}
