Name:    urlview
Version: 0.9
Release: %mkrel 16

Summary: A URL extractor/viewer for use with Mutt
License: GPL
Group:   Networking/Mail
Url:     ftp://ftp.mutt.org/mutt/contrib/
Source0: ftp://ftp.mutt.org/mutt/contrib/%{name}-%{version}.tar.bz2
Source1: urlview-regex.o-alpha.bz2
Patch0 : urlview-comma.patch2
Patch1:  urlview-0.9-use_firefox.patch
# fix #54424: fix segfault when opening an url
Patch2:  urlview-0.9-fix_segfault.patch

BuildRequires: slang
BuildRequires: slang-devel
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: slang >= 0.99.38
Requires: webclient

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .firefox
%patch2 -b .segfault

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
