# aqua-copr

COPR packaging for [aqua](https://github.com/aquaproj/aqua), a declarative CLI
version manager written in Go.

## Install

```sh
dnf copr enable mvahebi/aqua
dnf install aqua
```

## How it works

- [`aqua.spec`](aqua.spec) builds the upstream release tarball from
  `aquaproj/aqua` tags.
- A push to `main` triggers COPR's webhook, which rebuilds and publishes the
  updated package.

Building requires networking enabled on the COPR project, since `go build`
fetches module dependencies at build time (no vendored modules are bundled).

## License

Packaging in this repository is provided under the [LICENSE](LICENSE)
(MIT), matching upstream aqua's license.
