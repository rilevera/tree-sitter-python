# @rilevera/tree-sitter-python

Rilevera's WebAssembly distribution of the Python grammar for [tree-sitter].
The package contains the compiled `tree-sitter-python.wasm` grammar and no
native language bindings.

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

Run `make` to list the repository commands. Rebuild the generated parser and
WASM artifact from a clean state with:

```sh
make parser-clean
make test
make parser-build
```

`make clean` and `make build` are shorter aliases for those commands.

Package versions can be changed with:

```sh
make set-version VERSION=1.2.3
make bump-minor
make bump-patch
```

Each version command updates `package.json` and `tree-sitter.json` together.
Build, test, and publish the configured version to GitHub Packages with:

```sh
make publish
```

```sh
bun install
make test
make build
```

`make build` always regenerates the grammar and parser sources, runs the grammar
tests, and then writes the committed package artifact to
`tree-sitter-python.wasm` at the repository root.
