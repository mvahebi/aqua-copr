Name:           aqua
Version:        2.63.0
Release:        1%{?dist}
Summary:        Declarative CLI version manager
License:        MIT
URL:            https://github.com/aquaproj/aqua
Source0:        https://github.com/aquaproj/aqua/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang

%undefine _debugsource_packages

%description
A declarative CLI version manager written in Go. Aqua supports lazy
installation, registries, continuous updates, and seamless CLI
version switching.

%prep
%autosetup -n aqua-%{version}

%build
export CGO_ENABLED=0
export GOFLAGS="-trimpath"
export GOTOOLCHAIN=auto
go build -buildvcs=false -ldflags "-X main.version=v%{version}" -o out/aqua ./cmd/aqua

%install
install -Dpm0755 out/aqua %{buildroot}%{_bindir}/aqua

%check
%{buildroot}%{_bindir}/aqua --version

%files
%license LICENSE
%doc README.md
%{_bindir}/aqua

%changelog
* Wed Sep 23 2026 mvahebi - 2.63.0-1
- Update to 2.63.0
