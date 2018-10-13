#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-B-Hooks-EndOfScope
Version  : 0.24
Release  : 11
URL      : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.24.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/B-Hooks-EndOfScope-0.24.tar.gz
Summary  : 'Execute code after a scope finished compilation'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-B-Hooks-EndOfScope-data = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)

%description
This archive contains the distribution B-Hooks-EndOfScope,
version 0.24:
Execute code after a scope finished compilation

%package data
Summary: data components for the perl-B-Hooks-EndOfScope package.
Group: Data

%description data
data components for the perl-B-Hooks-EndOfScope package.


%package dev
Summary: dev components for the perl-B-Hooks-EndOfScope package.
Group: Development
Requires: perl-B-Hooks-EndOfScope-data = %{version}-%{release}
Provides: perl-B-Hooks-EndOfScope-devel = %{version}-%{release}

%description dev
dev components for the perl-B-Hooks-EndOfScope package.


%prep
%setup -q -n B-Hooks-EndOfScope-0.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-B-Hooks-EndOfScope
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-B-Hooks-EndOfScope/LICENCE
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
/usr/lib/perl5/vendor_perl/5.26.1/B/Hooks/EndOfScope.pm
/usr/lib/perl5/vendor_perl/5.26.1/B/Hooks/EndOfScope/PP.pm
/usr/lib/perl5/vendor_perl/5.26.1/B/Hooks/EndOfScope/PP/FieldHash.pm
/usr/lib/perl5/vendor_perl/5.26.1/B/Hooks/EndOfScope/PP/HintHash.pm
/usr/lib/perl5/vendor_perl/5.26.1/B/Hooks/EndOfScope/XS.pm

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-B-Hooks-EndOfScope/LICENCE

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/B::Hooks::EndOfScope.3
/usr/share/man/man3/B::Hooks::EndOfScope::PP.3
/usr/share/man/man3/B::Hooks::EndOfScope::XS.3
