"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateBuild = validateBuild;
const elements_1 = require("../data/elements");
const rules_1 = require("./rules");
const safety_1 = require("./safety");
function validateBuild(input) {
    const ruleChecks = [];
    for (const part of input.parts) {
        if (!elements_1.PART_CATEGORIES.includes(part.category)) {
            ruleChecks.push({ rule: 'part-category', passed: false, message: `Unknown category: ${part.category}` });
            continue;
        }
        if (!elements_1.ELEMENTS[part.atomicNumber]) {
            ruleChecks.push({ rule: 'known-element', passed: false, message: `Unknown atomic number: ${part.atomicNumber}` });
        }
    }
    const derivedNumbers = (0, rules_1.deriveNumbers)(input.numbers);
    ruleChecks.push(...(0, rules_1.runRuleChecks)(input, derivedNumbers));
    const safety = (0, safety_1.getSafetyStatus)(input.intents);
    for (const reason of safety.reasons) {
        ruleChecks.push({ rule: 'safety', passed: false, message: reason });
    }
    const allPassed = ruleChecks.every((c) => c.passed);
    const status = allPassed ? 'valid build' : 'rule broken';
    const suggestions = [];
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
//# sourceMappingURL=validator.js.map