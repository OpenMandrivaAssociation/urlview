Name:		urlview
Version:	0.9
Release:	18

Summary:	A URL extractor/viewer for use with Mutt
License:	GPL
Group:		Networking/Mail
Url:		ftp://ftp.mutt.org/mutt/contrib/
Source0:	ftp://ftp.mutt.org/mutt/contrib/%{name}-%{version}.tar.bz2
Source1:	urlview-regex.o-alpha.bz2
Patch0:		urlview-comma.patch2
Patch1:		urlview-0.9-use_firefox.patch
# fix #54424: fix segfault when opening an url
Patch2:		urlview-0.9-fix_segfault.patch

BuildRequires:	autoconf automake libtool
BuildRequires:	slang-devel

Requires:	webclient

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

# We need NEWS to make autoreconf happy
touch NEWS
autoreconf -fi
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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9-17mdv2011.0
+ Revision: 670750
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-16mdv2011.0
+ Revision: 608116
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-15mdv2010.1
+ Revision: 524305
- rebuilt for 2010.1

* Fri Oct 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.9-14mdv2010.0
+ Revision: 456299
- bumping mkrrel
- firefox should come before lynx
- netscape is dead, using firefox
- sanitize spec file
- fix #54424: fix segfault when opening an url

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9-13mdv2010.0
+ Revision: 427483
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.9-12mdv2009.1
+ Revision: 351450
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9-11mdv2009.0
+ Revision: 225908
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9-10mdv2008.1
+ Revision: 179673
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Fri Jun 08 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.9-9mdv2008.0
+ Revision: 37557
- Rebuild with libslang2.


* Wed Aug 09 2006 bcornec
+ 08/09/06 18:24:19 (54987)
Fix Bug 14200 (http://qa.mandriva.com/show_bug.cgi?id=14200)

* Wed Aug 09 2006 bcornec
+ 08/09/06 18:12:28 (54985)
import urlview-0.9-7mdk

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.9-7mdk
- Rebuild

