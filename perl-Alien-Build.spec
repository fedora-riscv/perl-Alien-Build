# Run optional test
%{bcond_without perl_Alien_Build_enables_optional_test}

Name:           perl-Alien-Build
Version:        1.36
Release:        2%{?dist}
Summary:        Build external dependencies for use in CPAN
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Alien-Build/
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-Build-%{version}.tar.gz
# Support only the most advanced pkgconfig implementation,
# the files are deleted in prep section
Patch0:         Alien-Build-1.36-Remove-redundant-pkgconfig-implementations.patch
# Do not require C++ for build ing C tests, bug #923024,
# <https://github.com/Perl5-Alien/Alien-Build/pull/53>
Patch1:         Alien-Build-1.36-corpus-cmake-libpalindrome-is-in-C.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Which) >= 1.10
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
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
BuildRequires:  perl(Acme::Alien::DontPanic) >= 0.026
# Break build cycle: perl-Alien-Base-ModuleBuild → perl-Alien-Build
BuildRequires:  perl(Alien::Base::ModuleBuild) >= 0.040
%endif
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Env::ShellWords)
# FFI::Platypus not packaged
BuildRequires:  perl(HTTP::Tiny) >= 0.044
# PkgConfig not packaged
BuildRequires:  perl(Readonly) >= 1.60
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(URI::file)
%endif
# make in the lib/Alien/Build/Plugin/Build/CMake.pm plugin
# make in the lib/Alien/Build/Plugin/Build/Make.pm plugin
# make or Alien::gmake
BuildRequires:  make
Suggests:       curl
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
Suggests:       wget
# Alien::Base::PkgConfig moved from perl-Alien-Base-ModuleBuild
Conflicts:      perl-Alien-Base-ModuleBuild < 1.00

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
# Alien::Build::Plugin::PkgConfig::LibPkgConf,
# MANIFEST is updated by Remove-redundant-pkgconfig-implementations.patch
%patch0 -p1
rm lib/Alien/Build/Plugin/PkgConfig/{CommandLine,PP}.pm 
rm t/alien_build_plugin_pkgconfig_{commandline,pp}.t
%patch1 -p1

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
* Fri Feb 23 2018 Petr Pisar <ppisar@redhat.com> - 1.36-2
- Do not require C++ for build ing C tests (bug #923024)

* Tue Feb 06 2018 Petr Pisar <ppisar@redhat.com> - 1.36-1
- 1.36 bump

* Mon Nov 06 2017 Petr Pisar <ppisar@redhat.com> - 1.32-1
- 1.32 bump

* Fri Nov 03 2017 Petr Pisar <ppisar@redhat.com> - 1.28-2
- Conflict with perl-Alien-Base-ModuleBuild < 1.00 because of
  Alien::Base::PkgConfig

* Fri Nov 03 2017 Petr Pisar <ppisar@redhat.com> - 1.28-1
- 1.28 bump

* Tue Sep 26 2017 Petr Pisar <ppisar@redhat.com> - 1.18-1
- 1.18 bump

* Tue Sep 19 2017 Petr Pisar <ppisar@redhat.com> - 1.16-1
- 1.16 bump

* Fri Sep 08 2017 Petr Pisar <ppisar@redhat.com> - 1.10-1
- 1.10 bump

* Tue Aug 29 2017 Petr Pisar <ppisar@redhat.com> - 1.05-1
- 1.05 bump

* Mon Aug 28 2017 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Fri Aug 18 2017 Petr Pisar <ppisar@redhat.com> - 0.99-1
- 0.99 bump

* Thu Aug 17 2017 Petr Pisar <ppisar@redhat.com> 0.95-1
- Specfile autogenerated by cpanspec 1.78.
