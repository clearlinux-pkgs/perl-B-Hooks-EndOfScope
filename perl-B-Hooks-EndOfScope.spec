#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v4
# autospec commit: e738c51
#
Name     : perl-B-Hooks-EndOfScope
Version  : 0.28
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.28.tar.gz
Summary  : 'Execute code after a scope finished compilation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-B-Hooks-EndOfScope-license = %{version}-%{release}
Requires: perl-B-Hooks-EndOfScope-perl = %{version}-%{release}
Requires: perl(Module::Implementation)
Requires: perl(Sub::Exporter::Progressive)
Requires: perl(Variable::Magic)
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution B-Hooks-EndOfScope,
version 0.28:
Execute code after a scope finished compilation

%package dev
Summary: dev components for the perl-B-Hooks-EndOfScope package.
Group: Development
Provides: perl-B-Hooks-EndOfScope-devel = %{version}-%{release}
Requires: perl-B-Hooks-EndOfScope = %{version}-%{release}

%description dev
dev components for the perl-B-Hooks-EndOfScope package.


%package license
Summary: license components for the perl-B-Hooks-EndOfScope package.
Group: Default

%description license
license components for the perl-B-Hooks-EndOfScope package.


%package perl
Summary: perl components for the perl-B-Hooks-EndOfScope package.
Group: Default
Requires: perl-B-Hooks-EndOfScope = %{version}-%{release}

%description perl
perl components for the perl-B-Hooks-EndOfScope package.


%prep
%setup -q -n B-Hooks-EndOfScope-0.28
cd %{_builddir}/B-Hooks-EndOfScope-0.28
pushd ..
cp -a B-Hooks-EndOfScope-0.28 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Hooks-EndOfScope
cp %{_builddir}/B-Hooks-EndOfScope-%{version}/LICENCE %{buildroot}/usr/share/package-licenses/perl-B-Hooks-EndOfScope/92e9290ceb2e9a59d7faa69aa7bc9e314c060618 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::Hooks::EndOfScope.3
/usr/share/man/man3/B::Hooks::EndOfScope::PP.3
/usr/share/man/man3/B::Hooks::EndOfScope::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-Hooks-EndOfScope/92e9290ceb2e9a59d7faa69aa7bc9e314c060618

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
