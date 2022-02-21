#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Hooks-EndOfScope
Version  : 0.26
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.26.tar.gz
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

%description
This archive contains the distribution B-Hooks-EndOfScope,
version 0.26:
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
%setup -q -n B-Hooks-EndOfScope-0.26
cd %{_builddir}/B-Hooks-EndOfScope-0.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/B-Hooks-EndOfScope-0.26/LICENCE %{buildroot}/usr/share/package-licenses/perl-B-Hooks-EndOfScope/eb95c6fdb9efb5a60092b8dfff9c5e6fd7c4f80c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::Hooks::EndOfScope.3
/usr/share/man/man3/B::Hooks::EndOfScope::PP.3
/usr/share/man/man3/B::Hooks::EndOfScope::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-B-Hooks-EndOfScope/eb95c6fdb9efb5a60092b8dfff9c5e6fd7c4f80c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/B/Hooks/EndOfScope.pm
/usr/lib/perl5/vendor_perl/5.34.0/B/Hooks/EndOfScope/PP.pm
/usr/lib/perl5/vendor_perl/5.34.0/B/Hooks/EndOfScope/PP/FieldHash.pm
/usr/lib/perl5/vendor_perl/5.34.0/B/Hooks/EndOfScope/PP/HintHash.pm
/usr/lib/perl5/vendor_perl/5.34.0/B/Hooks/EndOfScope/XS.pm
