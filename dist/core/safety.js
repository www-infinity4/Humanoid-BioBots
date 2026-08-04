"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.getSafetyStatus = getSafetyStatus;
const BLOCKED_TERMS = [
    'weapon', 'kill', 'suicide', 'torture', 'fight', 'terrorism', 'nukes'
];
function getSafetyStatus(intents) {
    if (!intents || intents.length === 0) {
        return { safety: 'green', reasons: [] };
    }
    const lower = intents.map((x) => x.toLowerCase());
    const hits = BLOCKED_TERMS.filter((term) => lower.some((i) => i.includes(term)));
    if (hits.length > 0) {
        return { safety: 'red', reasons: hits.map((h) => `Blocked intent detected: ${h}`) };
    }
    const cautionTerms = ['gambling', 'alcohol', 'drug'];
    const cautionHits = cautionTerms.filter((term) => lower.some((i) => i.includes(term)));
    if (cautionHits.length > 0) {
        return { safety: 'yellow', reasons: cautionHits.map((h) => `Caution intent detected: ${h}`) };
    }
    return { safety: 'green', reasons: [] };
}
//# sourceMappingURL=safety.js.map