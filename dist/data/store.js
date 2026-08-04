"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.saveBuild = saveBuild;
exports.listBuilds = listBuilds;
const builds = [];
function saveBuild(build) {
    builds.push(build);
    return build;
}
function listBuilds() {
    return builds;
}
//# sourceMappingURL=store.js.map