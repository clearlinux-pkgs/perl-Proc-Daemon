#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Proc-Daemon
Version  : 0.23
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/A/AK/AKREAL/Proc-Daemon-0.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AK/AKREAL/Proc-Daemon-0.23.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libproc-daemon-perl/libproc-daemon-perl_0.23-1.debian.tar.xz
Summary  : 'Run Perl program(s) as a daemon process'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Proc-Daemon-license
Requires: perl-Proc-Daemon-man
BuildRequires : perl(Proc::ProcessTable)

%description
# Summary
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

%package license
Summary: license components for the perl-Proc-Daemon package.
Group: Default

%description license
license components for the perl-Proc-Daemon package.


%package man
Summary: man components for the perl-Proc-Daemon package.
Group: Default

%description man
man components for the perl-Proc-Daemon package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Proc-Daemon-0.23
mkdir -p %{_topdir}/BUILD/Proc-Daemon-0.23/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Proc-Daemon-0.23/deblicense/

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
mkdir -p %{buildroot}/usr/share/doc/perl-Proc-Daemon
cp LICENSE %{buildroot}/usr/share/doc/perl-Proc-Daemon/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Proc/Daemon.pm
/usr/lib/perl5/site_perl/5.26.1/Proc/Daemon.pod

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Proc-Daemon/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Proc::Daemon.3
