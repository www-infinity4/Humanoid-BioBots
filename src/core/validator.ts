import { ELEMENTS, PART_CATEGORIES } from '../data/elements';
import { deriveNumbers, runRuleChecks } from './rules';
import { getSafetyStatus } from './safety';
import { BuildInput, ValidationResult } from '../types/models';

export function validateBuild(input: BuildInput): ValidationResult {
  const ruleChecks = [];

  for (const part of input.parts) {
    if (!PART_CATEGORIES.includes(part.category as (typeof PART_CATEGORIES)[number])) {
      ruleChecks.push({ rule: 'part-category', passed: false, message: `Unknown category: ${part.category}` });
      continue;
    }
    if (!ELEMENTS[part.atomicNumber]) {
      ruleChecks.push({ rule: 'known-element', passed: false, message: `Unknown atomic number: ${part.atomicNumber}` });
    }
  }

  const derivedNumbers = deriveNumbers(input.numbers);
  ruleChecks.push(...runRuleChecks(input, derivedNumbers));

  const safety = getSafetyStatus(input.intents);
  for (const reason of safety.reasons) {
    ruleChecks.push({ rule: 'safety', passed: false, message: reason });
  }

  const allPassed = ruleChecks.every((c) => c.passed);
  const status: ValidationResult['status'] = allPassed ? 'valid build' : 'rule broken';
  const suggestions: string[] = [];

  if (!ruleChecks.find((c) => c.rule === 'required-pair-15-43' && c.passed)) {
    suggestions.push('Add both 15 (P) and 43 (Tc) to satisfy required pair rule.');
  }
  if (ruleChecks.find((c) => c.rule === 'forbidden-pair-51-34' && !c.passed)) {
    suggestions.push('Remove 34 or 51; this pair is forbidden.');
  }
  if (ruleChecks.find((c) => c.rule === '51-companion-rule' && !c.passed)) {
    suggestions.push('When using 51, include one companion number: 9, 0, 92, or 10 (maps to 3).');
  }
  if (safety.safety === 'red') {
    suggestions.push('Remove blocked intents to continue.');
  }

  return {
    status,
    safety: safety.safety,
    ruleChecks,
    suggestions,
    derivedNumbers
  };
}
