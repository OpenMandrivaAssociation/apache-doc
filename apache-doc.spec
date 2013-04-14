# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The apache Manual
Name:		apache-doc
Version:	2.4.3
Release:	1
Group:		System/Servers
License:	Apache License
URL:		http://www.apache.org
Source0:	manual.conf
Requires(pre):	apache-conf >= %{version}
Requires:	apache-conf >= %{version}
BuildRequires:	apache-source = %{version}
BuildArch:	noarch

%description
This package contains the apache server documentation in HTML format.

Please view the documentaion by starting the apache server and your favourite
web browser and point to this URL: http://localhost/manual

%prep

%setup -c -T
cp -dpR %{_usrsrc}/apache-%{version}/docs/manual .

cp %{SOURCE0} manual.conf
perl -pi -e "s|_DOCDIR_|%{_docdir}/%{name}|g" manual.conf

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

%build

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -m0644 manual.conf %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/00_manual.conf

cat > README.MDV << EOF
Please view the documentaion by starting the apache server and your favourite
web browser and point to this URL: http://localhost/manual

Accessing the HTML manual manually on the filesystem can be tricky, you will have
to do something like this first:

cd %{_docdir}/%{name}
for i in \`find -name "*.html.en"\`; do
    new_name=\`echo \$i | sed -e "s/.html.en/.html/g"\`
    mv -f \$i \$new_name
done

lynx index.html

EOF

%files
%doc manual/* README.MDV
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/00_manual.conf


%changelog
* Fri Sep 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.21-0.1
- built for updates

* Wed Sep 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.21-1mdv2012.0
+ Revision: 699747
- 2.2.21

* Thu Sep 01 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.20-1
+ Revision: 697666
- 2.2.20

* Tue Jun 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.19-1
+ Revision: 684991
- bump release

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.19-0
+ Revision: 676778
- 2.2.19 (pre-release)

* Sat May 14 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.18-1
+ Revision: 674418
- 2.2.18

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.17-2
+ Revision: 662769
- mass rebuild

* Wed Oct 20 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.17-1mdv2011.0
+ Revision: 586896
- 2.2.17

* Sat Mar 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.15-1mdv2010.1
+ Revision: 515158
- 2.2.15 (official)

* Tue Mar 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.15-0.0mdv2010.1
+ Revision: 513532
- 2.2.15 (pre-release)

* Mon Mar 01 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.14-2mdv2010.1
+ Revision: 513195
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise
- don't duplicate spec-helper job

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.14-1mdv2010.0
+ Revision: 453381
- 2.2.14 was silently released 23-Sep-2009

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.14-0.1mdv2010.0
+ Revision: 451693
- 2.2.14 (pre-release)

* Mon Aug 10 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.13-1mdv2010.0
+ Revision: 414350
- 2.2.13

* Wed Jul 29 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.12-1mdv2010.0
+ Revision: 402992
- 2.2.12

* Mon Feb 02 2009 Oden Eriksson <oeriksson@mandriva.com> 2.2.11-2mdv2009.1
+ Revision: 336378
- pick up changes

* Tue Dec 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.11-1mdv2009.1
+ Revision: 314831
- 2.2.11

* Mon Oct 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-1mdv2009.1
+ Revision: 295606
- 2.2.10

* Fri Jun 13 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-1mdv2009.0
+ Revision: 218817
- 2.2.9

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.8-2mdv2008.1
+ Revision: 181431
- rebuild

* Fri Jan 18 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.8-1mdv2008.1
+ Revision: 154718
- 2.2.8 (official release)

* Fri Jan 11 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.8-0.1mdv2008.1
+ Revision: 147924
- 2.2.8

* Sat Jan 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.7-0.1mdv2008.1
+ Revision: 145822
- 2.2.7

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.6-1mdv2008.0
+ Revision: 82351
- 2.2.6 (release)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.5-0.1mdv2008.0
+ Revision: 64313
- 2.2.5

