Summary:	BSD database library for C
Summary(pl):	Biblioteka C do obs³ugi baz Berkeley DB
Name:		db
Version:	4.0.14
Release:	3.2
License:	GPL
Group:		Libraries
Source0:	http://www.berkeleydb.com/update/snapshot/%{name}-%{version}.tar.gz
#Patch0:		%{name}-static.patch
#Patch1:		%{name}-linux.patch
#Patch2:		%{name}-jbj.patch
Patch0:		%{name}-rpm.patch
URL:		http://www.berkeleydb.com/
#BuildRequires:	glibc-static
%{?_with_java:BuildRequires:	java}
BuildRequires:	tcl-devel >= 8.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%description -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley db jest u¿ywana wielu aplikacjach, w tym w
Pythonie i Perlu.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Summary(pl):	Narzêdzia do obs³ugi baz Berkeley DB z linii poleceñ
Group:		Applications/Databases
Requires:	%{name} = %{version}

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB
databases.

%description utils -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³ugje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera narzêdzia do obs³ugi baz Berkeley DB z linii
poleceñ.

%package tcl
Summary:	Berkeley database library for TCL
Summary(pl):	Biblioteka baz danych Berkeley dla TCL
Group:		Development/Languages/Tcl
Requires:	tcl

%description tcl
Berkeley database library for TCL.

%description tcl -l pl
Biblioteka baz danych Berkeley dla TCL.

%package cxx
Summary:	Berkeley database library for C++
Summary(pl):	Biblioteka baz danych Berkeley dla C++
Group:		Libraries

%description cxx
Berkeley database library for C++.

%description cxx -l pl
Biblioteka baz danych Berkeley dla C++.

%package java
Summary:	Berkeley database library for Java
Summary(pl):	Biblioteka baz danych Berkeley dla Java
Group:		Libraries

%description java
Berkeley database library for Java.

%description java -l pl
Biblioteka baz danych Berkeley dla Java.

%package devel
Summary:	Header files for Berkeley database library
Summary(pl):	Pliki nag³ówkowe do biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%description devel -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³ugje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê do budowania
programów u¿ywaj±cych Berkeley DB.

%package static
Summary:	Static libraries for Berkeley database library
Summary(pl):	Statyczne biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the static libraries for building programs which
use Berkeley DB.

%description static -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³ugje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera statyczne biblioteki do budowania programów
u¿ywaj±cych Berkeley DB.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
cp -a build_unix build_unix.static

cd build_unix.static

CFLAGS="%{rpmcflags} -fno-rtti -fno-implicit-templates" \
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-implicit-templates" \
../dist/configure \
	--prefix=%{_prefix} \
	--enable-compat185 \
	--disable-shared \
	--enable-static \
	--enable-rpc \
	--enable-cxx

# (temporarily?) disabled because of compilation errors:
#	--enable-dump185 \

%{__make} library_build

cd ../build_unix

CFLAGS="%{rpmcflags} -fno-rtti -fno-implicit-templates" \
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-implicit-templates" \

%if %{?_with_java:1}%{!?_with_java:0}
../dist/configure \
	--prefix=%{_prefix} \
	--enable-compat185 \
	--enable-shared \
	--disable-static \
	--enable-rpc \
	--enable-cxx \
	--enable-tcl \
	--with-tcl=%{_libdir} \
	--enable-java
%else
../dist/configure \
	--prefix=%{_prefix} \
	--enable-compat185 \
	--enable-shared \
	--disable-static \
	--enable-rpc \
	--enable-cxx \
	--enable-tcl \
	--with-tcl=/usr/lib
%endif

%{__make} library_build TCFLAGS='-I$(builddir) -I%{_includedir}'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir},/lib}

cd build_unix.static

%{__make} library_install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

cd ../build_unix

%{__make} library_install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	LIB_INSTALL_FILE_LIST=""

#mv -f $RPM_BUILD_ROOT%{_libdir}/libdb-*.so $RPM_BUILD_ROOT/lib
#ln -sf ../../lib/libdb-3.1.so $RPM_BUILD_ROOT%{_libdir}/libdb.so
#ln -sf ../../lib/libdb-3.1.so $RPM_BUILD_ROOT%{_libdir}/libdb3.so
#ln -sf ../../lib/libdb-3.1.so $RPM_BUILD_ROOT%{_libdir}/libdb-3.1.so
#ln -sf libdb-3.1.a $RPM_BUILD_ROOT%{_libdir}/libdb.a
#ln -sf libdb3.so $RPM_BUILD_ROOT%{_libdir}/libndbm.so
#ln -sf libdb3.a $RPM_BUILD_ROOT%{_libdir}/libndbm.a

cd ..
#rm -rf examples_java
#cp -a java/src/com/sleepycat/examples examples_java

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
#%attr(755,root,root) /lib/libdb-*.so
%attr(755,root,root) %{_libdir}/libdb-*.so

%files utils
%defattr(644,root,root,755)
%doc docs/utility/*
%attr(755,root,root) %{_bindir}/berkeley_db_svc
%attr(755,root,root) %{_bindir}/db*_archive
%attr(755,root,root) %{_bindir}/db*_checkpoint
%attr(755,root,root) %{_bindir}/db*_deadlock
%attr(755,root,root) %{_bindir}/db*_dump
#%attr(755,root,root) %{_bindir}/db*_dump185
%attr(755,root,root) %{_bindir}/db*_load
%attr(755,root,root) %{_bindir}/db*_printlog
%attr(755,root,root) %{_bindir}/db*_recover
%attr(755,root,root) %{_bindir}/db*_stat
%attr(755,root,root) %{_bindir}/db*_upgrade
%attr(755,root,root) %{_bindir}/db*_verify

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-*.so

%if %{?_with_java:1}%{!?_with_java:0}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_java*.so
%attr(644,root,root) %{_libdir}/db.jar
%endif

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_tcl-*.so

%files devel
%defattr(644,root,root,755)
%doc docs/{api*,ref,index.html,sleepycat,images} examples_c*
%attr(755,root,root) %{_libdir}/libdb*.la
#%attr(755,root,root) %{_libdir}/libdb.so
%attr(755,root,root) %{_libdir}/libdb*.so
#%attr(755,root,root) %{_libdir}/libndbm.so
#%attr(755,root,root) %{_libdir}/libdb_tcl.so
#%attr(755,root,root) %{_libdir}/libdb_cxx.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
