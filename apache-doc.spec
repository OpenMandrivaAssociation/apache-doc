# (oe) undefining these makes the build _real_ quick.
%undefine __find_provides
%undefine __find_requires

Summary:	The apache Manual
Name:		apache-doc
Version:	2.2.14
Release:	%mkrel 1
Group:		System/Servers
License:	Apache License
URL:		http://www.apache.org
Source0:	manual.conf
Requires(pre):	apache-conf >= %{version}
Requires:	apache-conf >= %{version}
BuildRequires:	apache-source = %{version} file
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

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

%post
if [ -f %{_var}/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2
fi
    
%postun
if [ "$1" = "0" ]; then
    if [ -f %{_var}/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc manual/* README.MDV
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/00_manual.conf
