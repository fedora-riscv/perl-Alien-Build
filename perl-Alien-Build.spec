# Run optional test
%{bcond_without perl_Alien_Build_enables_optional_test}

# Remove after packaging Acme::Alien::DontPanic
%global perl_bootstrap 1

Name:           perl-Alien-Build
Version:        0.99
Release:        1%{?dist}
Summary:        Build external dependencies for use in CPAN
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Alien-Build/
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Which) >= 1.10
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
%if !%{defined perl_bootstrap}
# Build cycle: perl-Alien-cmake3 → perl-Alien-Build
BuildRequires:  perl(Alien::cmake3) >= 0.02
%endif
# Archive::Tar or (tar and bzip2 and gzip and xz)
BuildRequires:  perl(Archive::Tar)
# Archive::Zip or unzip
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(base)
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::INI::Reader::Multiline)
BuildRequires:  perl(constant)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(FFI::CheckLib)
# FFI::Platypus is optional and not packaged
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::BOM)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Tiny) >= 0.077
# Alien::Build::Plugin::PkgConfig::Negotiate finds a pkgconfig implementation
# in this order:
# PkgConfig::LibPkgConf 0.04, pkgconf, pkg-config, PkgConfig 0.14026
# We selected the most advanced PkgConfig::LibPkgConf and removed the other
# plugins.
BuildRequires:  perl(PkgConfig::LibPkgConf::Client) >= 0.04
BuildRequires:  perl(PkgConfig::LibPkgConf::Util) >= 0.04
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require) >= 0.000060
BuildRequires:  perl(Text::ParseWords) >= 3.26
# YAML or Data::Dumper
BuildRequires:  perl(YAML)
# Tests:
# AnyEvent not used
# AnyEvent::FTP::Server not used
BuildRequires:  perl(File::Glob)
# Getopt::Long not used
BuildRequires:  perl(HTTP::Tiny)
# IO::Socket::INET not used
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
# Mojo::JSON not used
# Mojo::URL not used
# Mojolicious::Lite not used
BuildRequires:  perl(Net::FTP)
# Proc::Daemon not used
BuildRequires:  perl(Test2::Mock) >= 0.000060
BuildRequires:  perl(Test2::Require::Module) >= 0.000060
BuildRequires:  perl(Test2::V0) >= 0.000060
# URI not used
%if %{with perl_Alien_Build_enables_optional_test}
# Optional tests:
%if !%{defined perl_bootstrap}
# Break build cycle: Acme::Alien::DontPanic → Test::Alien
# Acme::Alien::DontPanic not yet packaged
%endif
BuildRequires:  perl(Alien::Base::ModuleBuild)
BuildRequires:  perl(Alien::Base::PkgConfig)
BuildRequires:  perl(Env::ShellWords)
# FFI::Platypus not packaged
# PkgConfig not packaged
BuildRequires:  perl(Test::Exec)
BuildRequires:  perl(URI::file)
%endif
# make in the lib/Alien/Build/Plugin/Build/CMake.pm plugin
# make in the lib/Alien/Build/Plugin/Build/Make.pm plugin
# make or Alien::gmake
BuildRequires:  make
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
%if !%{defined perl_bootstrap}
# Build cycle: perl-Alien-cmake3 → perl-Alien-Build
Requires:       perl(Alien::cmake3) >= 0.02
%endif
# Archive::Tar or (tar and bzip2 and gzip and xz)
Requires:       perl(Archive::Tar)
# Archive::Zip or unzip
Requires:       perl(Archive::Zip)
Requires:       perl(Config::INI::Reader::Multiline)
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::ParseXS) >= 3.30
Requires:       perl(FFI::CheckLib)
Requires:       perl(File::BOM)
Requires:       perl(File::Find)
Requires:       perl(Path::Tiny) >= 0.077
# Alien::Build::Plugin::PkgConfig::Negotiate finds a pkgconfig implementation
# in this order:
# PkgConfig::LibPkgConf 0.04, pkgconf, pkg-config, PkgConfig 0.14026
# We selected the most advanced PkgConfig::LibPkgConf and removed the other
# plugins.
Requires:       perl(PkgConfig::LibPkgConf::Client) >= 0.04
Requires:       perl(PkgConfig::LibPkgConf::Util) >= 0.04
Requires:       perl(Storable)
Requires:       perl(Test2::API) >= 1.302015
Requires:       perl(Test2::Require) >= 0.000060
Requires:       perl(Text::ParseWords) >= 3.26
# YAML or Data::Dumper
Requires:       perl(YAML)

# Do not gather dependencies from the documentation
%{?perl_default_filter}

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Capture::Tiny|Path::Tiny|Test2::API|Test2::Require|Text::ParseWords)\\)$

%description
This package provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at run time.

%prep
%setup -q -n Alien-Build-%{version}
# Remove redundant pkgconfig implementations, keep
# Alien::Build::Plugin::PkgConfig::LibPkgConf
rm lib/Alien/Build/Plugin/PkgConfig/{CommandLine,PP}.pm 
sed -i -r -e '\,lib/Alien/Build/Plugin/PkgConfig/(CommandLine|PP)\.pm,d' \
    Makefile.PL MANIFEST
rm t/alien_build_plugin_pkgconfig_{commandline,pp}.t
sed -i -r -e '\,^t/alien_build_plugin_pkgconfig_(commandline|pp)\.t,d' \
    MANIFEST
sed -i -r -e '\,Alien::Build::Plugin::PkgConfig::(CommandLine|PP),d' \
    t/01_use.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes* example README SUPPORT
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 0.99-1
- 0.99 bump

* Thu Aug 17 2017 Petr Pisar <ppisar@redhat.com> 0.95-1
- Specfile autogenerated by cpanspec 1.78.
