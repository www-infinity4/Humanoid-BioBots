import { StoredBuild } from '../types/models';

const builds: StoredBuild[] = [];

export function saveBuild(build: StoredBuild): StoredBuild {
  builds.push(build);
  return build;
}

export function listBuilds(): StoredBuild[] {
  return builds;
}
