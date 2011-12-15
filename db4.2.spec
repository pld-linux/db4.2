#
# Conditional build:
%bcond_without	java		# don't build Java library
%bcond_without	tcl		# don't build Tcl bindings
%bcond_with	pmutex		# use process-shared POSIX mutexes (not available with linuxthreads)
%bcond_with	nptl		# use process-shared POSIX mutexes (NPTL provides full interface)
%bcond_without	static_libs	# don't build static libraries
%bcond_with	default_db	# use this db as default system db
#
%define		ver		4.2.52
%define		patchlevel	5
%{?with_nptl:%define	with_pmutex	1}
Summary:	Berkeley DB database library for C
Summary(pl.UTF-8):	Biblioteka C do obsługi baz Berkeley DB
Name:		db4.2
Version:	%{ver}.%{patchlevel}
Release:	1
License:	Sleepycat public license (GPL-like, see LICENSE)
Group:		Libraries
#Source0Download: http://www.oracle.com/technetwork/database/berkeleydb/downloads/index-082944.html
Source0:	http://download.oracle.com/berkeley-db/db-%{ver}.tar.gz
# Source0-md5:	cbc77517c9278cdb47613ce8cb55779f
%patchset_source -f http://download.oracle.com/berkeley-db/patches/db/%{ver}/patch.%{ver}.%g 1 %{patchlevel}
Patch0:		db-so-suffix.patch
Patch1:		%{name}-amd64-fastmutex.patch
URL:		http://www.oracle.com/technetwork/database/berkeleydb/downloads/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	rpmbuild(macros) >= 1.426
BuildRequires:	sed >= 4.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.0}
%if %{with default_db}
Provides:	db = %{version}-%{release}
Obsoletes:	db4
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{without default_db}
%define		_includedir	%{_prefix}/include/db4.2
%endif

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%description -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley db jest używana w wielu aplikacjach, w tym w
Pythonie i Perlu.

%package devel
Summary:	Header files for Berkeley database library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with default_db}
Provides:	db-devel = %{version}-%{release}
Obsoletes:	db-devel
Obsoletes:	db3-devel
Obsoletes:	db4-devel
%endif

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%description devel -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera pliki nagłówkowe i dokumentację do budowania
programów używających Berkeley DB.

%package static
Summary:	Static libraries for Berkeley database library
Summary(pl.UTF-8):	Statyczne biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-static = %{version}-%{release}
Obsoletes:	db-static
Obsoletes:	db3-static
Obsoletes:	db4-static
%endif

%description static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the static libraries for building programs which
use Berkeley DB.

%description static -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera statyczne biblioteki do budowania programów
używających Berkeley DB.

%package cxx
Summary:	Berkeley database library for C++
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla C++
Group:		Libraries
%if %{with default_db}
Provides:	db-cxx = %{version}-%{release}
Obsoletes:	db4-cxx
%endif

%description cxx
Berkeley database library for C++.

%description cxx -l pl.UTF-8
Biblioteka baz danych Berkeley dla C++.

%package cxx-devel
Summary:	Header files for db-cxx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-devel = %{version}-%{release}
Obsoletes:	db-cxx-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description cxx-devel
Header files for db-cxx library.

%description cxx-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki db-cxx.

%package cxx-static
Summary:	Static version of db-cxx library
Summary(pl.UTF-8):	Statyczna wersja biblioteki db-cxx
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}
%if %{with default_db}
Provides:	db-cxx-static = %{version}-%{release}
Obsoletes:	db-cxx-static
%endif
Conflicts:	db-static < 4.2.50-1

%description cxx-static
Static version of db-cxx library.

%description cxx-static -l pl.UTF-8
Statyczna wersja biblioteki db-cxx.

%package java
Summary:	Berkeley database library for Java
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Javy
Group:		Libraries
Requires:	jpackage-utils
%if %{with default_db}
Provides:	db-java = %{version}-%{release}
Obsoletes:	db-java
%endif

%description java
Berkeley database library for Java.

%description java -l pl.UTF-8
Biblioteka baz danych Berkeley dla Javy.

%package java-devel
Summary:	Development files for db-java library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-java
Group:		Development/Languages/Java
Requires:	%{name}-java = %{version}-%{release}
%if %{with default_db}
Provides:	db-java-devel = %{version}-%{release}
Obsoletes:	db-java-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description java-devel
Development files for db-java library.

%description java-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-java.

%package tcl
Summary:	Berkeley database library for Tcl
Summary(pl.UTF-8):	Biblioteka baz danych Berkeley dla Tcl
Group:		Development/Languages/Tcl
Requires:	tcl
%if %{with default_db}
Provides:	db-tcl = %{version}-%{release}
Obsoletes:	db4-tcl
%endif

%description tcl
Berkeley database library for Tcl.

%description tcl -l pl.UTF-8
Biblioteka baz danych Berkeley dla Tcl.

%package tcl-devel
Summary:	Development files for db-tcl library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki db-tcl
Group:		Development/Languages/Tcl
Requires:	%{name}-tcl = %{version}-%{release}
%if %{with default_db}
Provides:	db-tcl-devel = %{version}-%{release}
Obsoletes:	db-tcl-devel
%endif
Conflicts:	db-devel < 4.1.25-3

%description tcl-devel
Development files for db-tcl library.

%description tcl-devel -l pl.UTF-8
Pliki programistyczne biblioteki db-tcl.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Summary(pl.UTF-8):	Narzędzia do obsługi baz Berkeley DB z linii poleceń
Group:		Applications/Databases
Requires:	%{name} = %{version}-%{release}
%if %{with default_db}
Provides:	db-utils = %{version}-%{release}
Obsoletes:	db-utils
Obsoletes:	db3-utils
Obsoletes:	db4-utils
%endif

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB
databases.

%description utils -l pl.UTF-8
Berkeley Database (Berkeley DB) to zestaw narzędzi programistycznych
zapewniających obsługę baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obsługuje dostęp do bazy przez B-drzewa i
funkcje mieszające ze stałą lub zmienną wielkością rekordu,
transakcje, kroniki, pamięć dzieloną i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera narzędzia do obsługi baz Berkeley DB z linii
poleceń.

%prep
%setup -q -n db-%{ver}
# official patches
%patchset_patch 1 %{patchlevel}

%patch0 -p1
%patch1 -p1

%if %{without nptl}
sed -i -e 's,AM_PTHREADS_SHARED("POSIX/.*,:,' dist/aclocal/mutex.ac
%endif

sed -i -e '/AC_PROG_LIBTOOL/aLT_OUTPUT' dist/configure.ac

%build
cd dist
cp -f /usr/share/aclocal/libtool.m4 aclocal/libtool.ac
cp -f /usr/share/aclocal/ltoptions.m4 aclocal/ltoptions.ac
cp -f /usr/share/aclocal/ltsugar.m4 aclocal/ltsugar.ac
cp -f /usr/share/aclocal/ltversion.m4 aclocal/ltversion.ac
cp -f /usr/share/aclocal/lt~obsolete.m4 aclocal/lt~obsolete.ac
cp -f /usr/share/automake/config.sub .
cp -f /usr/share/libtool/config/ltmain.sh .
sh s_config
cd ..

%if %{with static_libs}
cp -a build_unix build_unix.static

cd build_unix.static

CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
LDFLAGS="%{rpmcflags} %{rpmldflags}"
export CC CXX CFLAGS CXXFLAGS LDFLAGS

../dist/%configure \
	--disable-shared \
	--enable-static \
	--enable-compat185 \
	--enable-cxx \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-rpc

# (temporarily?) disabled because of compilation errors:
#	--enable-dump185 \

%{__make} library_build
cd ..
%endif

cd build_unix

../dist/%configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-shared \
	--disable-static \
	--enable-compat185 \
	--enable-cxx \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-rpc \
	%{?with_java:--enable-java} \
	%{?with_tcl:--enable-tcl --with-tcl=/usr/lib}

%{__make} library_build \
	TCFLAGS='-I$(builddir) -I%{_includedir}' \
	LIBSO_LIBS="\$(LIBS)" \
	LIBTSO_LIBS="\$(LIBS) -ltcl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}
%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%endif

%if %{with static_libs}
%{__make} -C build_unix.static library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}
%endif

%{__make} -C build_unix library_install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_INSTALL_FILE_LIST="" \
	docdir=%{_docdir}/db-%{version}-docs \
	includedir=%{_includedir}

%if %{with default_db}
install -d $RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT%{_libdir}/libdb-4.2.so $RPM_BUILD_ROOT/%{_lib}
%endif

cd $RPM_BUILD_ROOT%{_libdir}
%if %{with static_libs}
mv -f libdb.a libdb-4.2.a
mv -f libdb_cxx.a libdb_cxx-4.2.a
%endif
%if %{with java}
mv -f $RPM_BUILD_ROOT%{_libdir}/db.jar $RPM_BUILD_ROOT%{_javadir}/db-4.2.jar
%endif
%if %{with default_db}
ln -sf /%{_lib}/libdb-4.2.so libdb.so
ln -sf /%{_lib}/libdb-4.2.so libdb4.so
ln -sf /%{_lib}/libdb-4.2.so libdb-4.2.so
ln -sf /%{_lib}/libdb-4.2.so libndbm.so
ln -sf libdb-4.2.la libdb.la
ln -sf libdb-4.2.la libdb4.la
ln -sf libdb-4.2.la libndbm.la
ln -sf libdb_cxx-4.2.so libdb_cxx.so
ln -sf libdb_cxx-4.2.la libdb_cxx.la
%if %{with java}
ln -sf libdb_java-4.2.la libdb_java.la
ln -sf db-4.2.jar $RPM_BUILD_ROOT%{_javadir}/db.jar
%endif
%if %{with tcl}
ln -sf libdb_tcl-4.2.so libdb_tcl.so
ln -sf libdb_tcl-4.2.la libdb_tcl.la
%endif
%if %{with static_libs}
ln -sf libdb-4.2.a libdb.a
ln -sf libdb-4.2.a libdb4.a
ln -sf libdb-4.2.a libndbm.a
ln -sf libdb_cxx-4.2.a libdb_cxx.a
%endif
%endif

sed -i "s/old_library=''/old_library='libdb-4.2.a'/" libdb-4.2.la
sed -i "s/old_library=''/old_library='libdb_cxx-4.2.a'/" libdb_cxx-4.2.la

cd -

cd $RPM_BUILD_ROOT%{_bindir}
mv -f berkeley_db_svc berkeley_db_svc-4.2
%{?with_default_db:ln -sf berkeley_db_svc-4.2 berkeley_db_svc}
for F in db_*; do
  Fver=$(echo $F|sed 's/db_/db4.2_/')
  mv $F $Fver
  %{?with_default_db:ln -sf $Fver $F}
done
cd -
rm -f examples_c*/tags
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}
cp -rf examples_c/* $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}
cp -rf examples_cxx/* $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}

%if %{with java}
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
cp -rf examples_java/* $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
%else
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/db-%{version}-docs/java
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%if %{with default_db}
%attr(755,root,root) /%{_lib}/libdb-4.2.so
%else
%attr(755,root,root) %{_libdir}/libdb-4.2.so
%endif
%dir %{_docdir}/db-%{version}-docs
%{_docdir}/db-%{version}-docs/sleepycat
%{_docdir}/db-%{version}-docs/index.html

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdb-4.2.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb-4.2.so
%attr(755,root,root) %{_libdir}/libdb4.so
%attr(755,root,root) %{_libdir}/libdb.so
%attr(755,root,root) %{_libdir}/libndbm.so
%{_libdir}/libdb4.la
%{_libdir}/libdb.la
%{_libdir}/libndbm.la
%else
%dir %{_includedir}
%endif
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_docdir}/db-%{version}-docs/api_c
%{_docdir}/db-%{version}-docs/images
%{_docdir}/db-%{version}-docs/ref
%{_examplesdir}/db-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdb-4.2.a
%if %{with default_db}
%{_libdir}/libdb4.a
%{_libdir}/libdb.a
%{_libdir}/libndbm.a
%endif
%endif

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-4.2.so

%files cxx-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-4.2.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_cxx.so
%{_libdir}/libdb_cxx.la
%endif
%{_includedir}/db_cxx.h
%{_docdir}/db-%{version}-docs/api_cxx
%{_examplesdir}/db-cxx-%{version}

%if %{with static_libs}
%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-4.2.a
%if %{with default_db}
%{_libdir}/libdb_cxx.a
%endif
%endif

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_java-4.2.so
%{_javadir}/db-4.2.jar
%if %{with default_db}
%{_javadir}/db.jar
%endif

%files java-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_java-4.2.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_java.so
%{_libdir}/libdb_java.la
%endif
%{_docdir}/db-%{version}-docs/java
%{_examplesdir}/db-java-%{version}
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_tcl-4.2.so

%files tcl-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_tcl-4.2.la
%if %{with default_db}
%attr(755,root,root) %{_libdir}/libdb_tcl.so
%{_libdir}/libdb_tcl.la
%endif
%{_docdir}/db-%{version}-docs/api_tcl
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/berkeley_db_svc-4.2
%attr(755,root,root) %{_bindir}/db4.2_archive
%attr(755,root,root) %{_bindir}/db4.2_checkpoint
%attr(755,root,root) %{_bindir}/db4.2_deadlock
%attr(755,root,root) %{_bindir}/db4.2_dump
#%attr(755,root,root) %{_bindir}/db4.2_dump185
%attr(755,root,root) %{_bindir}/db4.2_load
%attr(755,root,root) %{_bindir}/db4.2_printlog
%attr(755,root,root) %{_bindir}/db4.2_recover
%attr(755,root,root) %{_bindir}/db4.2_stat
%attr(755,root,root) %{_bindir}/db4.2_upgrade
%attr(755,root,root) %{_bindir}/db4.2_verify
%if %{with default_db}
%attr(755,root,root) %{_bindir}/berkeley_db_svc
%attr(755,root,root) %{_bindir}/db_archive
%attr(755,root,root) %{_bindir}/db_checkpoint
%attr(755,root,root) %{_bindir}/db_deadlock
%attr(755,root,root) %{_bindir}/db_dump
#%attr(755,root,root) %{_bindir}/db_dump185
%attr(755,root,root) %{_bindir}/db_load
%attr(755,root,root) %{_bindir}/db_printlog
%attr(755,root,root) %{_bindir}/db_recover
%attr(755,root,root) %{_bindir}/db_stat
%attr(755,root,root) %{_bindir}/db_upgrade
%attr(755,root,root) %{_bindir}/db_verify
%endif
%{_docdir}/db-%{version}-docs/utility
