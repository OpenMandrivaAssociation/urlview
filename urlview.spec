Name:    urlview
Version: 0.9
Release: 18

Summary: A URL extractor/viewer for use with Mutt
License: GPLv2+
Group:   Networking/Mail
Url:     ftp://ftp.mutt.org/mutt/contrib/
Source0: ftp://ftp.mutt.org/mutt/contrib/%{name}-%{version}.tar.bz2
Patch0 : urlview-comma.patch2
Patch1:  urlview-0.9-use_firefox.patch
# fix #54424: fix segfault when opening an url
Patch2:  urlview-0.9-fix_segfault.patch

BuildRequires: slang-devel

Requires: webclient

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .firefox
%patch2 -b .segfault
# this should've been created by passing -i to autoreconf...?
touch NEWS
autoreconf -fi

%build
#suckattack
%configure --with-slang
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall
install -m755 url_handler.sh %{buildroot}%{_bindir}/url_handler.sh

%files
%doc AUTHORS ChangeLog COPYING
%doc INSTALL README sample.urlview 
%doc urlview.sgml
%{_bindir}/urlview
%{_bindir}/url_handler.sh
%{_mandir}/man1/urlview.1*
