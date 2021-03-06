AR = ['/usr/bin/ar']
ARCH_ST = ['-arch']
ARFLAGS = ['rcs']
BASH = ['/bin/bash']
BINDIR = '/usr/local/bin'
BOOST_VERSION = '1_59'
BOOST_VERSION_NUMBER = 105900
CC_VERSION = ('8', '0', '0')
COMPILER_CXX = 'clang++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/clang++']
CXXFLAGS = ['-O2', '-g', '-pedantic', '-Wall', '-Wextra', '-Wno-unused-parameter', '-fcolor-diagnostics', '-Wno-unused-local-typedef', '-std=c++11', '-stdlib=libc++']
CXXFLAGS_BOOST = ['']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PCAP_SET_IMMEDIATE_MODE = ['-Wno-error']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXXPCH_EXT = '.pch'
CXXPCH_F = ['-include']
CXXPCH_FLAGS = ['-x', 'c++-header']
CXX_NAME = 'clang'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['NDEBUG']
DEFINES_BOOST = ['BOOST_LOG_DYN_LINK']
DEFINES_NDN_CXX = ['HAVE_NDN_CXX=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'mac-o'
DEST_CPU = 'x86_64'
DEST_OS = 'darwin'
DOCDIR = '/usr/local/share/doc/nfd'
DOXYGEN = ['/opt/local/bin/doxygen']
DVIDIR = '/usr/local/share/doc/nfd'
EXEC_PREFIX = '/usr/local'
FRAMEWORKPATH_ST = '-F%s'
FRAMEWORK_NDN_CXX = ['CoreFoundation', 'Security']
FRAMEWORK_ST = ['-framework']
HAVE_ASIO_PCAP_SUPPORT = True
HAVE_IS_MOVE_CONSTRUCTIBLE = True
HAVE_LIBPCAP = True
HAVE_LIBRESOLV = True
HAVE_NDN_CXX = 1
HAVE_UNIX_SOCKETS = True
HAVE_WEBSOCKET = True
HTMLDIR = '/usr/local/share/doc/nfd'
INCLUDEDIR = '/usr/local/include'
INCLUDES_BOOST = '/opt/local/include'
INCLUDES_NDN_CXX = ['/usr/local/include', '/opt/local/include']
INCLUDES_WEBSOCKET = '/Users/Mocca/Desktop/NFD/websocketpp'
INFODIR = '/usr/local/share/info'
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_BOOST = ['/opt/local/lib']
LIBPATH_NDN_CXX = ['/usr/local/lib', '/opt/local/lib']
LIBPATH_ST = '-L%s'
LIB_BOOST = ['boost_system-mt', 'boost_chrono-mt', 'boost_program_options-mt', 'boost_thread-mt', 'boost_log-mt', 'boost_log_setup-mt']
LIB_LIBPCAP = ['pcap']
LIB_LIBRESOLV = ['resolv']
LIB_NDN_CXX = ['ndn-cxx', 'boost_system-mt', 'boost_filesystem-mt', 'boost_date_time-mt', 'boost_iostreams-mt', 'boost_regex-mt', 'boost_program_options-mt', 'boost_chrono-mt', 'boost_thread-mt', 'boost_log-mt', 'boost_log_setup-mt', 'cryptopp', 'ssl', 'crypto', 'sqlite3', 'pthread']
LIB_ST = '-l%s'
LINKFLAGS = ['-stdlib=libc++']
LINKFLAGS_BOOST = ['']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cxxshlib = ['-dynamiclib', '-Wl,-compatibility_version,1', '-Wl,-current_version,1']
LINKFLAGS_cxxstlib = []
LINK_CXX = ['/usr/bin/clang++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'nfd'
PDFDIR = '/usr/local/share/doc/nfd'
PKGCONFIG = ['/opt/local/bin/pkg-config']
PREFIX = '/usr/local'
PSDIR = '/usr/local/share/doc/nfd'
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = []
SONAME_ST = []
SPHINX_BUILD = ['/opt/local/bin/sphinx-build']
STLIBPATH_BOOST = ['/opt/local/lib']
STLIBPATH_ST = '-L%s'
STLIB_BOOST = []
STLIB_MARKER = []
STLIB_ST = '-l%s'
SYSCONFDIR = '/usr/local/etc'
TAR = ['/usr/bin/tar']
WEBSOCKET_VERSION = ['0', '7', '0']
WITH_PCH = True
cfg_files = ['/Users/Mocca/Desktop/NFD/build/core/config.hpp']
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.dylib'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
