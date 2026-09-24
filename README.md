# @rilevera/tree-sitter-python

Rilevera's WebAssembly distribution of the Python grammar for [tree-sitter].
The package contains the compiled `tree-sitter-python.wasm` grammar, its
TypeScript path declaration, and no native language bindings.

[tree-sitter]: https://tree-sitter.github.io/tree-sitter/

## Installation

Configure the `@rilevera` scope to use GitHub Packages and authenticate with a
token that can read packages:

```ini
@rilevera:registry=https://npm.pkg.github.com
```

Then install the package with your consuming application's package manager.
The package root and `@rilevera/tree-sitter-python/tree-sitter-python.wasm`
both resolve to the WASM artifact.

## Development

Development and publishing require Bun `>=1.3.6 <1.3.12`.

Run `make` to list the repository commands.

```bash
make install    # validate Bun and install dependencies from the lockfile
make test       # regenerate the parser and run the grammar tests
make test-wasm  # run the corpus tests against tree-sitter-python.wasm via web-tree-sitter
make build      # generate, build, and test tree-sitter-python.wasm
```

`make test` runs the corpus tests against a native build produced by the tree-sitter CLI —
useful for fast feedback while iterating on the grammar. Since the published package ships
WebAssembly instead, `make build` (and `make publish`) verify the built `tree-sitter-python.wasm`
itself by re-running the corpus tests through `web-tree-sitter`, which can behave differently
from the CLI's native build.

Run `make help` to see all available commands.

`tree-sitter-python.wasm` is a build artifact — it's gitignored, not committed. Run `make build`
to generate it locally before publishing or testing against a consumer.

### Testing against a consumer locally

To try a change here in a downstream project before tagging a release:

1. `make build` in this repo to regenerate `tree-sitter-python.wasm`.
2. In the consumer's `package.json`, point the dependency at this checkout:
   `"@rilevera/tree-sitter-python": "file:../tree-sitter-python"` (adjust the path), then run its
   install command.
3. Re-run `make build` here as you iterate — since the dependency is a symlink, the consumer
   picks up the change without reinstalling.

Revert the consumer's `package.json`/lockfile to the tagged or registry version once you're
done testing.

## Releasing

Package versions can be changed with:

```sh
make set-version VERSION=1.2.3
make bump-minor
make bump-patch
```

Each version command updates `package.json` and `tree-sitter.json` together.
Commit the version bump, then push a matching tag. Pushing a tag triggers the
`Publish package` GitHub Actions workflow, which builds, tests, and publishes
the package to GitHub Packages.

To publish locally instead, run:

```sh
make publish
```
