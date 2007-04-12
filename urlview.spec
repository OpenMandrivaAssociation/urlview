%define name	urlview
%define version	0.9
%define release	%mkrel 8

Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Mail
Source: %{name}-%{version}.tar.bz2
URL: ftp://ftp.mutt.org/mutt/contrib/
Requires: slang >= 0.99.38, webclient
Source1: urlview-regex.o-alpha.bz2
Patch: urlview-comma.patch2
Patch1: url_path.patch
Buildroot: %{_tmppath}/%{name}-buildroot
Summary: A URL extractor/viewer for use with Mutt.
BuildRequires: slang-devel slang

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q 
%patch -p1
%patch1 -p1

%build
#suckattack
%ifarch alpha
mkdir regex
bzcat %{SOURCE1} > regex/regex.o
%endif
%configure --with-slang
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
%makeinstall
install -m755 url_handler.sh $RPM_BUILD_ROOT%{_bindir}/url_handler.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%doc INSTALL README sample.urlview 
%doc urlview.sgml
%{_bindir}/urlview
%{_bindir}/url_handler.sh
%{_mandir}/man1/urlview.1*


