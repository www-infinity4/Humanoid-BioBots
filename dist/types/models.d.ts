export type RobotPartCategory = 'structure' | 'power' | 'sensors' | 'wiring' | 'shielding';
export interface ElementInfo {
    atomicNumber: number;
    symbol: string;
    name: string;
    category: RobotPartCategory;
}
export interface RobotPartSelection {
    category: RobotPartCategory;
    atomicNumber: number;
}
export interface BuildInput {
    name: string;
    parts: RobotPartSelection[];
    numbers: number[];
    intents?: string[];
}
export interface RuleCheck {
    rule: string;
    passed: boolean;
    message: string;
}
export interface ValidationResult {
    status: 'valid build' | 'rule broken';
    safety: 'green' | 'yellow' | 'red';
    ruleChecks: RuleCheck[];
    suggestions: string[];
    derivedNumbers: number[];
}
export interface StoredBuild {
    id: string;
    input: BuildInput;
    validation: ValidationResult;
    createdAt: string;
}
//# sourceMappingURL=models.d.ts.map