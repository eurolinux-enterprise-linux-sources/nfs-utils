Summary: NFS utilities and supporting clients and daemons for the kernel NFS server
Name: nfs-utils
URL: http://sourceforge.net/projects/nfs
Version: 1.3.0
Release: 0.48%{?dist}.3
Epoch: 1

# group all 32bit related archs
%define all_32bit_archs i386 i486 i586 i686 athlon ppc sparcv9

Source0: https://www.kernel.org/pub/linux/utils/nfs-utils/%{version}/%{name}-%{version}.tar.xz

Source1: id_resolver.conf
Source2: nfs.sysconfig
Source3: nfs-utils_env.sh
Source4: lockd.conf
Source5: 24-nfs-server.conf

#
# RHEL7.1
#
Patch001: nfs-utils-1.3.0-rpcgssd-timeout.patch
Patch002: nfs-utils-1.3.0-statd-callback.patch
Patch003: nfs-utils-1.3.0-mountd-start-statd-path.patch
Patch004: nfs-utils-1.3.0-rpcgssd-noerror-message.patch
Patch005: nfs-utils-1.3.0-rpcgssd-acceptor.patch
Patch006: nfs-utils-1.3.0-exportfs-NULL-pointer-test.patch
Patch007: nfs-utils-1.3.0-rpcgssd-errno-typo.patch
Patch008: nfs-utils-1.3.0-nfsiostat-output.patch
Patch009: nfs-utils-1.3.0-nfsclient-after.patch
Patch010: nfs-utils-1.3.0-startstatd-systemd.patch
Patch011: nfs-utils-1.3.0-gssproxy.patch
Patch012: nfs-utils-1.3.0-systemd-args.patch
Patch013: nfs-utils-1.3.0-libmount-umount-verbose.patch
Patch014: nfs-utils-1.3.0-mountd-dos.patch
Patch015: nfs-utils-1.3.0-exportfs-ipv6-arg.patch
Patch016: nfs-utils-1.3.0-exportfs-noreaddirplus.patch
Patch017: nfs-utils-1.3.0-systemd-idmapd.patch
Patch018: nfs-utils-1.3.0-systemd-ha-nonotify.patch
#
# RHEL7.2
#
Patch019: nfs-utils-1.3.0-blkmapd-pnfs.patch
Patch020: nfs-utils-1.3.0-mountstats-update.patch
Patch021: nfs-utils-1.3.0-mountd-v4root-sec.patch
Patch022: nfs-utils-1.3.0-systemd-idmapd-varlib.patch
Patch023: nfs-utils-1.3.0-nfsdcltrack-v2schema.patch
Patch024: nfs-utils-1.3.0-mountd-manpage-args.patch
Patch025: nfs-utils-1.3.0-mountd-manpage-netconfig.patch
Patch026: nfs-utils-1.3.0-systemd-rpcbind.patch
Patch027: nfs-utils-1.3.0-blkmapd-loop.patch
Patch028: nfs-utils-1.3.0-gssd-noclear-retval.patch
Patch029: nfs-utils-1.3.0-gssd-tgt-flood.patch
Patch030: nfs-utils-1.3.0-systemd-decouple.patch
#
# RHEL7.3
#
Patch031: nfs-utils-1.3.0-nfsidmap-timeout.patch
Patch032: nfs-utils-1.3.0-hostpton-eainoname.patch
Patch033: nfs-utils-1.3.0-rpcgssd-maccout-nocase.patch
Patch034: nfs-utils-1.3.0-nfsdcltrack-v2schema-update.patch
Patch035: nfs-utils-1.3.0-mountd-usage-error.patch
Patch036: nfs-utils-1.3.0-mountd-usage.patch
Patch037: nfs-utils-1.3.0-rpcgssd-debug.patch
Patch038: nfs-utils-1.3.0-start-statd-once.patch
Patch039: nfs-utils-1.2.9-exportfs-badentries.patch
Patch040: nfs-utils-1.3.0-mount-remount.patch
Patch041: nfs-utils-1.3.0-nfs_connect_nb-eintr.patch
Patch042: nfs-utils-1.3.0-statd-monlists.patch
Patch043: nfs-utils-1.3.0-nfsidmap-update.patch
Patch044: nfs-utils-1.3.0-mountstats-manpage-fix.patch
Patch045: nfs-utils-1.3.0-systemd-config.patch
Patch046: nfs-utils-1.3.0-exportfs-slashes.patch
Patch047: nfs-utils-1.3.0-exportfs-hostnames.patch
Patch048: nfs-utils-1.3.0-exportfs-bufsiz.patch
Patch049: nfs-utils-1.3.0-blkmapd-usage.patch
Patch050: nfs-utils-1.3.0-rpcidmapd-usage.patch
Patch051: nfs-utils-1.3.0-rpcgssd-multithread.patch
Patch052: nfs-utils-1.3.0-rpcgssd-findkeytab.patch
Patch053: nfs-utils-1.3.0-start-statd-root.patch
Patch054: nfs-utils-1.3.0-nfsd-rdma.patch
Patch055: nfs-utils-1.3.0-nfsd-warnings.patch
Patch056: nfs-utils-1.3.0-mountd-manpage-P.patch
Patch057: nfs-utils-1.3.0-mountstats-manpage-fix2.patch
Patch058: nfs-utils-1.3.0-mountd-netgroups.patch
Patch059: nfs-utils-1.3.0-umount-opt-typo.patch
Patch060: nfs-utils-1.3.0-mount-usage.patch
Patch061: nfs-utils-1.3.0-nfsidmap-h-opt.patch
Patch062: nfs-utils-1.3.0-exportfs-empty-exports.patch
Patch063: nfs-utils-1.3.0-statd-warnings.patch
Patch064: nfs-utils-1.3.0-start-statd-flock.patch
Patch065: nfs-utils-1.3.0-mountd-root.patch
Patch066: nfs-utils-1.3.0-mount-nfs-types.patch
#
# RHEL7.4
#
Patch067: nfs-utils-1.3.0-mount-default-v42.patch
Patch068: nfs-utils-1.3.0-gssd-default-tcp.patch
Patch069: nfs-utils-1.3.0-mountstats-pnfs.patch
Patch070: nfs-utils-1.3.0-nfsdcltrack-usage.patch
Patch071: nfs-utils-1.3.0-daemon_init-warning.patch
Patch072: nfs-utils-1.3.0-mount-v4arg-fix.patch
Patch073: nfs-utils-1.3.0-systemd-rpcpipefs.patch
Patch074: nfs-utils-1.3.0-mountd-filedes.patch
Patch075: nfs-utils-1.3.0-exportfs-redundant.patch
Patch076: nfs-utils-1.3.0-nfs-conf.patch
Patch077: nfs-utils-1.3.0-gssd-rdma-to-tcp.patch
Patch078: nfs-utils-1.3.0-gssd-thread-safe.patch
Patch079: nfs-utils-1.3.0-mount-uninit-structs.patch
Patch080: nfs-utils-1.3.0-exportfs-securitylabel.patch
Patch081: nfs-utils-1.3.0-mount-v41.patch
Patch082: nfs-utils-1.3.0-nfsstat-retval.patch
Patch083: nfs-utils-1.3.0-server-generator.patch
Patch084: nfs-utils-1.3.0-nfsman-minorversion.patch
Patch085: nfs-utils-1.3.0-rpcgssd-preferred-realm.patch
Patch086: nfs-utils-1.3.0-mountstats-iostats.patch
Patch087: nfs-utils-1.3.0-mount-prognotreg.patch
Patch088: nfs-utils-1.3.0-statd-notify-grace-period.patch
Patch089: nfs-utils-1.3.0-nfsstat-mounts.patch
Patch090: nfs-utils-1.3.0-nfsd-man-correction.patch
Patch091: nfs-utils-1.3.0-nfsdcltrack-errors.patch
Patch092: nfs-utils-1.3.0-systemd-network-online.patch
Patch093: nfs-utils-1.3.0-mount-explicit-rback.patch
Patch094: nfs-utils-1.3.0-systemd-gssproxy.patch
Patch095: nfs-utils-1.3.0-mount-use-minor-default.patch
Patch096: nfs-utils-1.3.0-mount-restore-econn.patch
Patch097: nfs-utils-1.3.0-exportfs-path-comp.patch
#
# RHEL7.4-Z
#
Patch098: nfs-utils-1.3.0-mount-addressfailed.patch
Patch099: nfs-utils-1.3.0-mount-eacces.patch
Patch100: nfs-utils-1.3.0-mount-minorversion.patch
Patch101: nfs-utils-1.3.0-mount-t-nfs4.patch

Patch1000: nfs-utils-1.2.1-statdpath-man.patch
Patch1001: nfs-utils-1.2.1-exp-subtree-warn-off.patch
Patch1002: nfs-utils-1.2.3-sm-notify-res_init.patch
Patch1003: nfs-utils-1.2.5-idmap-errmsg.patch

Group: System Environment/Daemons
Provides: exportfs    = %{epoch}:%{version}-%{release}
Provides: nfsstat     = %{epoch}:%{version}-%{release}
Provides: showmount   = %{epoch}:%{version}-%{release}
Provides: rpcdebug    = %{epoch}:%{version}-%{release}
Provides: rpc.idmapd  = %{epoch}:%{version}-%{release}
Provides: rpc.mountd  = %{epoch}:%{version}-%{release}
Provides: rpc.nfsd    = %{epoch}:%{version}-%{release}
Provides: rpc.statd   = %{epoch}:%{version}-%{release}
Provides: rpc.gssd    = %{epoch}:%{version}-%{release}
Provides: mount.nfs   = %{epoch}:%{version}-%{release}
Provides: mount.nfs4  = %{epoch}:%{version}-%{release}
Provides: umount.nfs  = %{epoch}:%{version}-%{release}
Provides: umount.nfs4 = %{epoch}:%{version}-%{release}
Provides: sm-notify   = %{epoch}:%{version}-%{release}
Provides: start-statd = %{epoch}:%{version}-%{release}

License: MIT and GPLv2 and GPLv2+ and BSD
Requires: rpcbind, sed, gawk, sh-utils, fileutils, textutils, grep
Requires: kmod, keyutils, quota
BuildRequires: libevent-devel libcap-devel
BuildRequires: libnfsidmap-devel libtirpc-devel >= 0.2.4-0.7 libblkid-devel
BuildRequires: krb5-libs >= 1.4 autoconf >= 2.57 openldap-devel >= 2.2
BuildRequires: automake, libtool, glibc-headers, device-mapper-devel
BuildRequires: krb5-devel, tcp_wrappers-devel, libmount-devel
BuildRequires: fedfs-utils-devel >= 0.8.0-7, sqlite-devel
Requires(pre): shadow-utils >= 4.0.3-25
Requires(pre): /sbin/chkconfig /sbin/nologin
Requires: libnfsidmap libevent
Requires: libtirpc >= 0.2.4-0.7 libblkid libcap libmount
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

Requires: gssproxy >= 0.7.0-3
Conflicts: gssproxy < 0.3.0-10

%description
The nfs-utils package provides a daemon for the kernel NFS server and
related tools, which provides a much higher level of performance than the
traditional Linux NFS server used by most users.

This package also contains the showmount program.  Showmount queries the
mount daemon on a remote host for information about the NFS (Network File
System) server on the remote host.  For example, showmount can display the
clients which are mounted on that host.

This package also contains the mount.nfs and umount.nfs program.

%prep
%setup -q

# 1009528 - have a configurable connection timeout for the rpcgssd service
%patch001 -p1
# 1108105 - "Adding callback on sm_notify" into nfs-utils on RHEL7
%patch002 -p1
# 1116794 - wrong PATH in /usr/sbin/start-statd
%patch003 -p1
# 1117384 - rpc.gssd always start fail, and no enough log/message to user
%patch004 -p1
# 1088011 - kerberized NFSv4.0 backchannel requests aren't authenticated properly by client
%patch005 -p1
# 1083018 - code defect support/export/hostname.c: host_pton() NULL pointer...
%patch006 -p1
# 1082480 - [gssd] code defects in get_servername()....
%patch007 -p1
# 1109864 - Man pages are not explaining the output of nfsiostat
%patch008 -p1
# 1144440 - Upgrade to latest upstream systemd scripts
%patch009 -p1
%patch010 -p1
# 1082746 - remove support for rpc.svcgssd
%patch011 -p1
# 170364 - Typos in nfs-utils sysconfig files and associated script
%patch012 -p1
# 923582 - umount -vvv not working 
%patch013 -p1
# 1163891 - rpc.mountd can be blocked by a bad client
%patch014 -p1
#  1161490 - [exportfs] when export [$IPv6]:$expdir always random fail
%patch015 -p1
# 1161458 - nfs-utils patch for Readdirplus / disable readdirplus
%patch016 -p1
# 1159234 - ocf:heartbeat:nfsserver does not umount /var/lib/nfs on shared disk
%patch017 -p1
# 1182692 - disable sm-notify on 'systemctl start nfs-server' no longer works
%patch018 -p1
# 1214821 - nfs-utils updates for block pnfs
%patch019 -p1
# 1215808 - Update mountstats command to the latest upstream version
%patch020 -p1
# 1187223 - rpc.mountd can set up pseudo exports without...
%patch021 -p1
# 1164064 - RHEL-7.1 regression fail: service nfs-idmapd start fail 
%patch022 -p1
# 1234598 - Early grace period expiry with NFSv4.1
%patch023 -p1
# 1003558 - In rpc.mountd man page -V -f -p -H and so on need and args 
%patch024 -p1
# 1196646 - man pages nfs/mount.fs should mention /etc/nfsmount.conf ...
%patch025 -p1
# 1171603 - Require rpcbind.service in nfs-server.service rather than ...
%patch026 -p1
# 237301 - blkmapd: Fix infinite loop when reading serial
%patch027 -p1
# 1087350 - [gssd] code defects in gssd_search_krb5_keytab()...
%patch028 -p1
# 1264999 - rpc.gssd fetches a TGT on every machine credential upcall
%patch029 -p1
# 1266993 - restarting rpbind also restart the the nfs server
%patch030 -p1
# 1161222 - nfsidmap not setting key timeouts 
%patch031 -p1
# 1276099 - exportfs -u incorrectly exits with a 1 whenever...
%patch032 -p1
# 1268040 - rpc.gssd should not assume that the machine account is in uppercase
%patch033 -p1
# 1285097 - updated nfs-utils package broke nfsdcltrack
%patch034 -p1
# 1003539 - If rpc.mountd specify options: "-N 2 -N 3 -N 4", should output...
%patch035 -p1
# 1003716 - rpc.mountd -h: 1. In help info not include -r|--reverse-lookup...
%patch036 -p1
# 1273163 - Allow gssd and svcgssd to set the libtirpc debug level
%patch037 -p1
# 1300007 - start-statd: don't run multiple rpc.statds on the one host.
%patch038 -p1
# 1287468 - Unable to start nfs server.service if any of the client is down...
%patch039 -p1
# 1313550 - Nondeterministic DNS lookups cause NFS kdump targets to fail
%patch040 -p1
# 1299003 - Unhandled EINTR during connection establishment leads...
%patch041 -p1
# 1284576 - lockd's and statd's monitor lists get out of sync
%patch042 -p1
# 1290488 Request a method(like a testperm) to show parameters of idmapd.conf
%patch043 -p1
# 1266013 - need to remove a few bogus .R macros of mountstats man page
%patch044 -p1
# 1331460 - nfs-config service is *not* being re-run as needed
%patch045 -p1
# 1276534 - exportfs -u cannot unexport when the specified...
%patch046 -p1
# 1331801 - exportfs -u can exit with status 1 if there are multiple...
%patch047 -p1
# 1243234 - exportfs: code defect, when export path length > 986...
%patch048 -p1
# 1001431 - RFE: feature blkmapd add help -h option, to output "usage:" info 
%patch049 -p1
# 1001438 - RFE: feature rpc.idmapd add help -h option, to output "usage:" info
%patch050 -p1
# 1331540 - multi-threaded rpc.gssd
%patch051 -p1
# 1334848 - cthon - rpc.gssd crash reading krb5.keytab in find_keytab_entry()
%patch052 -p1
# 1275082 - [vdsm] NFS mount fails sometimes with "rpc.statd is not running...
%patch053 -p1
# 1310691 - "--rdma" option of rpc.nfsd enables the wrong port
%patch054 -p1
# 1336419 - nfsd: Remove some warnings nfsd.c
%patch055 -p1
# 1037924 - [rpc.mountd] update rpc.mountd(8) manpage to change -P... 
%patch056 -p1
# 1263966 - typo in mountstats man page that should not contain "-s|--since"
%patch057 -p1
# 1341908 - rpc.mountd does not check for membership of IP...
%patch058 -p1
# 1246329 - umount.nfs -h/--help output typo with -f force unmount 
%patch059 -p1
# 1001443 - if no args specified, mount.nfs can not output the usage info
%patch060 -p1
# 1339877 - nfsidmap add help -h option to output usage info
%patch061 -p1
# 1340788 - [exportfs] should not fail on empty exports file with...
%patch062 -p1
# 1347030 - rpc.statd emits warnings like "Failed to delete:....
%patch063 -p1
# 1300007 - start-statd: don't run multiple rpc.statds on the one host. (v2)
%patch064 -p1
# 1353680 - NFSv4 export of "/" doesn't respect "crossmnt" export option 
%patch065 -p1
# 1363737 - man mount.nfs incorrectly mentions the default mount....
%patch066 -p1
# 1375259 - NFSv4.2 as default NFS mount protocol
%patch067 -p1
# 1386759 - nfs-utils requires a fix to support NFS/RDMA mounts....
%patch068 -p1
# 1377740 - Add pNFS READs and WRITEs to the mountstats program output 
%patch069 -p1
# 1001494 - RFE: feature, add "[Uu]sage:" string in the nfsdcltrack -h output info
%patch070 -p1
# 1377914 - Compiler Warning of support/nfs/mydaemon.c....
%patch071 -p1
# 1404617 - mount.nfs fall back to version 3 when specifying...
%patch072 -p1
# 1406164 - var-lib-nfs-rpc_pipefs.mount fails
%patch073 -p1
# 1409903 - Occasional SELinux denials when starting up knfsd
%patch074 -p1
# 1396402 - [exportfs] exportfs -s output some exports options twice, but..
%patch075 -p1
# 1418041 - Update nfs-utils to use latest upstream configuration style
%patch076 -p1
# 1386759 - nfs-utils requires a fix to support NFS/RDMA mounts....
%patch077 -p1
# 1419280 - Non-thread-safe functions used in multi-threaded rpc.gssd
%patch078 -p1
# 1415024 - [uninitialized struct] get wrong nfs version when doing nfs mount
%patch079 -p1
# 1435899 - exportfs: support "security_label" export option
%patch080 -p1
# 1435901 - mount.nfs: starts mount negation with v4.2 it should be v4.1 
%patch081 -p1
# 1400658 - nfsstat -m command returns false return code
%patch082 -p1
# 1437190 - nfs-server-generator: handle 'noauto' mounts correctly.
%patch083 -p1
# 1389827 - "minorversion=" mount option missing in nfs(5) man page
%patch084 -p1
# 1432643 - segfault in rpc.gssd in find_keytab_entry
%patch085 -p1
# 1400106 - mountstats: handle KeyError in accumulate_iostats
%patch086 -p1
# 1404121 - NFS fails to mount on boot if both client and server.... 
%patch087 -p1
# 1424599 - sm-notify ending grace period early can inhibit... 
%patch088 -p1
# 1425956 - nfsstat --mounts is unrecognized option
%patch089 -p1
# 1432750 - Manual page bug: two inaccuracies in nfsd(7) 
%patch090 -p1
# 1443176 - nfsdcltrack: Unable to prepare select statement...
%patch091 -p1
# 1409012 - nfs-server runs before network is ready...
%patch092 -p1
# 1447849 - mount.nfs4 falls back to version 3 when mounting...
%patch093 -p1
# 1459483 - nfs-utils need to cause gssproxy reload 
%patch094 -p1
# 1458504 mount.nfs: NFSv4 specified mount need to start negotiation...
%patch095 -p1
# 1404121 - NFS fails to mount on boot if both client and....
%patch096 -p1
# 1389046 Pacemaker node fenced out due to redundant export...
%patch097 -p1
# 1498959 - RHEL7.4: service nfs-server start fails the first time...
%patch098 -p1
# 1518718 - RHEL7.4: NFS mount to DELL/EMC Isilon servers fails...
%patch099 -p1
# 1547681 - nfs-utils: minorversion can't work
%patch100 -p1
# 1551927 - Incorrect NFS version string reported for NFSv4.2 mounts
%patch101 -p1

%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1

# Remove .orig files
find . -name "*.orig" | xargs rm -f

%build

%ifarch s390 s390x sparcv9 sparc64
PIE="-fPIE"
%else
PIE="-fpie"
%endif
export PIE

RELRO="-Wl,-z,relro,-z,now"

sh -x autogen.sh

CFLAGS="`echo $RPM_OPT_FLAGS $ARCH_OPT_FLAGS $PIE $RELRO -D_FILE_OFFSET_BITS=64`"
%configure \
    CFLAGS="$CFLAGS" \
    CPPFLAGS="$DEFINES" \
    LDFLAGS="-pie" \
    --enable-mountconfig \
    --enable-ipv6 \
	--with-statdpath=/var/lib/nfs/statd \
	--enable-libmount-mount \
	--with-systemd

make %{?_smp_mflags} all

%install
rm -rf $RPM_BUILD_ROOT/*

mkdir -p $RPM_BUILD_ROOT%/sbin
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/request-key.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
make DESTDIR=$RPM_BUILD_ROOT install
install -s -m 755 tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT%{_sbindir}
install -m 644 utils/mount/nfsmount.conf  $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 nfs.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/request-key.d
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/nfs

#
# Don't install code that is no longer supported
#
rm systemd/rpc-svcgssd.service
rm $RPM_BUILD_ROOT%{_sbindir}/rpc.svcgssd
rm $RPM_BUILD_ROOT%{_mandir}/man8/rpc.svcgssd.8
rm $RPM_BUILD_ROOT%{_mandir}/man8/svcgssd.8

mkdir -p $RPM_BUILD_ROOT/run/sysconfig
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/scripts
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gssproxy
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/usr/lib/systemd/scripts/nfs-utils_env.sh
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/lockd.conf
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/gssproxy

#
# For backwards compatablity 
#
cd $RPM_BUILD_ROOT%{_unitdir}
ln -s nfs-server.service nfs.service
ln -s rpc-gssd.service nfs-secure.service
ln -s rpc-gssd.service rpcgssd.service
ln -s nfs-idmapd.service  nfs-idmap.service
ln -s nfs-idmapd.service  rpcidmapd.service
ln -s rpc-statd.service nfs-lock.service
ln -s rpc-statd.service nfslock.service


mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rpc_pipefs

touch $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/rmtab
mv $RPM_BUILD_ROOT%{_sbindir}/rpc.statd $RPM_BUILD_ROOT/sbin

mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/statd/sm
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/statd/sm.bak
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/nfs/v4recovery
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/exports.d

%clean
rm -rf $RPM_BUILD_ROOT/*

%pre
# move files so the running service will have this applied as well
for x in gssd idmapd ; do
    if [ -f /var/lock/subsys/rpc.$x ]; then
		mv /var/lock/subsys/rpc.$x /var/lock/subsys/rpc$x
    fi
done

%define rpcuser_uid 29
# Create rpcuser gid as long as it does not already exist
cat /etc/group | cut -d':' -f 1 | grep --quiet rpcuser 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/groupadd -g %{rpcuser_uid} rpcuser >/dev/null 2>&1 || :
else
    /usr/sbin/groupmod -g %{rpcuser_uid} rpcuser >/dev/null 2>&1 || :
fi

# Create rpcuser uid as long as it does not already exist.
cat /etc/passwd | cut -d':' -f 1 | grep --quiet rpcuser 2>/dev/null
if [ "$?" -eq 1 ]; then
	/usr/sbin/useradd -l -c "RPC Service User" -r -g %{rpcuser_uid} \
		-s /sbin/nologin -u %{rpcuser_uid} -d /var/lib/nfs rpcuser >/dev/null 2>&1 || :
else
	/usr/sbin/usermod -u %{rpcuser_uid} -g %{rpcuser_uid} rpcuser >/dev/null 2>&1 || :
fi

# Using the 16-bit value of -2 for the nfsnobody uid and gid
%define nfsnobody_uid	65534

# Create nfsnobody gid as long as it does not already exist
cat /etc/group | cut -d':' -f 1 | grep --quiet nfsnobody 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/groupadd -g %{nfsnobody_uid} nfsnobody >/dev/null 2>&1 || :
else
    /usr/sbin/groupmod -g %{nfsnobody_uid} nfsnobody >/dev/null 2>&1 || :
fi

# Create nfsnobody uid as long as it does not already exist.
cat /etc/passwd | cut -d':' -f 1 | grep --quiet nfsnobody 2>/dev/null
if [ "$?" -eq 1 ]; then
    /usr/sbin/useradd -l -c "Anonymous NFS User" -r -g %{nfsnobody_uid} \
		-s /sbin/nologin -u %{nfsnobody_uid} -d /var/lib/nfs nfsnobody >/dev/null 2>&1 || :
else

   /usr/sbin/usermod -u %{nfsnobody_uid} -g %{nfsnobody_uid} nfsnobody >/dev/null 2>&1 || :
fi

%post
if [ $1 -eq 1 ] ; then
	# Initial installation
	/bin/systemctl enable nfs-client.target >/dev/null 2>&1 || :
	/bin/systemctl restart nfs-config  >/dev/null 2>&1 || :
fi
%systemd_post nfs-config
%systemd_post nfs-server

# Make sure statd used the correct uid/gid.
chown -R rpcuser:rpcuser /var/lib/nfs/statd

%preun
if [ $1 -eq 0 ]; then
	%systemd_preun nfs-client.target
	%systemd_preun nfs-server.server

    /usr/sbin/userdel rpcuser 2>/dev/null || :
    /usr/sbin/groupdel rpcuser 2>/dev/null || :
    /usr/sbin/userdel nfsnobody 2>/dev/null || :
    /usr/sbin/groupdel nfsnobody 2>/dev/null || :
    rm -rf /var/lib/nfs/statd
    rm -rf /var/lib/nfs/v4recovery
fi

%postun
if [ ! -f /etc/sysconfig/nfs-utils-disable-postun ]; then
	%systemd_postun_with_restart  nfs-client.target
	%systemd_postun_with_restart  nfs-server
	/bin/systemctl --system daemon-reload >/dev/null 2>&1 || :
fi

%posttrans
# clean up cruft left over by upgrade from versions < 1.3.0-0.8.el7
if [ -h /etc/systemd/system/multi-user.target.wants/nfs.target ]; then
	tgt=$(readlink /etc/systemd/system/multi-user.target.wants/nfs.target)
	if [ ! -e $tgt ]; then
		/bin/systemctl --quiet is-enabled nfs-server &>/dev/null
		reenable=$?
		rm -rf /etc/systemd/system/multi-user.target.wants/nfs.target &>/dev/null
		rm -rf /etc/systemd/system/nfs.target.wants &>/dev/null
		if [ $reenable ]; then
			/bin/systemctl --quiet reenable nfs-server &>/dev/null || :
		fi
	fi
fi

%triggerun -- nfs-utils < 1:1.2.9-0.5
/bin/systemctl stop nfs-secure.service >/dev/null 2>&1 || :
/bin/systemctl disable nfs-secure.service >/dev/null 2>&1 || :

%triggerun -- nfs-utils < 1:1.2.4-2
/bin/systemctl enable nfs-lock.service >/dev/null 2>&1 || :

%triggerin -- nfs-utils > 1:1.3.0-0.39
# reset configuration files and running daemons
if [ $1 -eq 2 ] ; then
	/bin/systemctl enable nfs-client.target >/dev/null 2>&1 || :
	/bin/systemctl restart nfs-config  >/dev/null 2>&1 || :
	/bin/systemctl reload-or-try-restart gssproxy >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/sysconfig/nfs
%config(noreplace) /etc/nfsmount.conf
%config(noreplace) /etc/nfs.conf
%dir %{_sysconfdir}/exports.d
%dir %{_sharedstatedir}/nfs/v4recovery
%dir %attr(555,root,root) %{_sharedstatedir}/nfs/rpc_pipefs
%dir %{_sharedstatedir}/nfs
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd/sm
%dir %attr(700,rpcuser,rpcuser) %{_sharedstatedir}/nfs/statd/sm.bak
%config(noreplace) %attr(644,rpcuser,rpcuser) %{_sharedstatedir}/nfs/state
%config(noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nfs/xtab
%config(noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nfs/etab
%config(noreplace) %verify(not md5 size mtime) %{_sharedstatedir}/nfs/rmtab
%config(noreplace) %{_sysconfdir}/request-key.d/id_resolver.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/lockd.conf
%attr(0600,root,root) %config(noreplace) /%{_sysconfdir}/gssproxy/24-nfs-server.conf
%doc linux-nfs/ChangeLog linux-nfs/KNOWNBUGS linux-nfs/NEW linux-nfs/README
%doc linux-nfs/THANKS linux-nfs/TODO
/sbin/rpc.statd
/sbin/osd_login
%{_sbindir}/exportfs
%{_sbindir}/nfsstat
%{_sbindir}/rpcdebug
%{_sbindir}/rpc.mountd
%{_sbindir}/rpc.nfsd
%{_sbindir}/showmount
%{_sbindir}/rpc.idmapd
%{_sbindir}/rpc.gssd
%{_sbindir}/sm-notify
%{_sbindir}/start-statd
%{_sbindir}/mountstats
%{_sbindir}/nfsiostat
%{_sbindir}/nfsidmap
%{_sbindir}/blkmapd
%{_sbindir}/nfsdcltrack
%{_mandir}/*/*
%{_unitdir}/*
%attr(755,root,root) /usr/lib/systemd/scripts/nfs-utils_env.sh
%{_prefix}/lib/systemd/system-generators/nfs-server-generator

%attr(4755,root,root)	/sbin/mount.nfs
/sbin/mount.nfs4
/sbin/umount.nfs
/sbin/umount.nfs4

%changelog
* Wed Mar 14 2018 Steve Dickson <steved@redhat.com> 1.3.0-0.48_4.3
- mount: move handling of "-t nfs4" into nfs_nfs_version() (bz 1551927)

* Thu Feb 22 2018 Steve Dickson <steved@redhat.com> 1.3.0-0.48_4.2
- mount: Fix problems with parsing minorversion= (bz 1547681)

* Thu Nov 30 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.48_4.1
- mount: handle EACCES during version negotiation (bz 1518718)

* Fri Oct  6 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.48_4
- rpc.nfsd: Do not fail when all address families are not support (bz 1450528)

* Mon Jun 19 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.48
- exportfs: fix path comparison in unexportfs_parsed() (bz 1389046)
- Correctly set the minor version when set in nfsmount.conf (1458504)

* Wed Jun 14 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.47
- mount.nfs: Restore errno after v3 mounts on ECONNREFUSED errors (bz 1404121)

* Mon Jun 12 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.46
- Use v4 minor default on all v4 mount types (bz 1458504)

* Wed Jun  7 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.45
- Restart gssproxy when the server is reloaded (bz 1459483)

* Thu Jun  1 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.44
- Updated patch for bz 1447849 with the upstream version (bz 1447849)

* Mon May 22 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.43
- mount: explicit v4 mounts should not roll back to v3 (bz 1447849)
- spec: Use reload-or-try-restart to restart gssproxy (bz 1440887)

* Tue May  9 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.42
- Removed RPCSVCGSSDARGS nfs.sysconfig (bz 1431218)

* Thu Apr 27 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.41
- nfsdcltrack: silence some expected errors (bz 1443176)
- Conditionally restart gssproxy now that config file is installed (bz 1440887)
- systemd: NFS server services should use network-online (bz 1409012)
- Cleaned up some fuzzy patches (bz 1409012)

* Sat Apr  8 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.40
- gssd: ensure that preferred_realm is non-NULL (bz 1432643)
- mountstats: handle KeyError in accumulate_iostats() (bz 1400106)
- mount: RPC_PROGNOTREGISTERED should not be a permanent error (bz 1404121)
- sm-notify: ending the grace period early should be configurable (bz 1424599)
- Fixed a couple typos that effected the '--mounts' nfsstat option (bz 1425956)
- Manual page bug: two inaccuracies in nfsd(7) (bz 1432750)

* Fri Mar 31 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.39
- nfsstats: fix some exit codes (bz 1400658)
- Added server-generator to improve ordering (bz 1437190)
- nfsman: document minorversion (bz 1389827)

* Tue Mar 28 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.38
- spec.conf: Added gssproxy server config file (bz 1431273)

* Tue Mar 28 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.37
- exportfs: support "security_label" export option (bz 1435899)
- svcgssd: Don't install code that is not suppported (bz 1431218)
- mount.nfs: start protocol negation with v4.1 instead of v4.2 (bz 1435901)
- nfs.conf: update nfs-conf.patch to include nfs.systemd.man (bz 1418041)

* Tue Feb 28 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.36
- exportfs: remove redundant exports options output (bz 1396402)
- Add /etc/nfs.conf support (bz 1418041)
- gssd: Convert 'rdma' to 'tcp' protocol (bz 1386759)
- gssd: replace non-thread-safe strtok with strsep (bz 1419280)
- mount: fix mount fail that caused by uninitialized struct (bz 1415024)

* Fri Jan  6 2017 Steve Dickson <steved@redhat.com> 1.3.0-0.35
- Fixed -o v4 from falling back to v3 (bz 1404617)
- systemd: Set var-lib-nfs-rpc_pipefs.mount After= tmpfiles (bz 1406164)
- mountd: talk to kernel using file descriptors instead of FILE (bz 1409903)

* Wed Dec  7 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.34
- mount.nfs: Start the mount negation with v4.2 (bz 1375259)
- gssd: Make TCP the default protocol for GSSD connections (bz 1386759)
- mountstats: add pNFS READs and WRITEs (bz 1377740)
- nfsdcltrack: Fixed typo in usage string (bz 1001494)
- mydaemon.c: Removed a warning (bz 1377914)

* Wed Aug 17 2016 Scott Mayhew <smayhew@redhat.com> 1.3.0-0.33
- spec: clean up cruft left over by upgrade from older versions (bz 1203765)

* Thu Aug  4 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.32
- mount.nfs.man, nfs.man: Update distinction between fstypes (bz 1363737)

* Mon Jul 11 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.31
- mountd: fix next_mnt handling for "/" (bz 1353680)

* Thu Jun 23 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.30
- statd: suppress a benign log message in nsm_delete_host() (bz 1347030)
- start-statd: Use flock to serialize the running of this script (bz 1300007)
- spec: update requires version of libtirpc-devel (bz 1346711)

* Thu Jun  9 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.29
- mountd: fix netgroup lookup for resolvable IP addresses (bz 1341908)
- umount: fixed typo in usage message (bz 1246329)
- mount.nfs: added usage output when no arguemnts are given (bz 1001443)
- nfsidmap: added the -h option (bz 1339877)
- exportfs: Do not fail on empty exports file (bz 1340788)

* Tue Jun  7 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.28
- Added max/min to nlm_timeout comment in lockd.conf (bz 1264387)

* Fri May 20 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.27
- nfsd: use correct byte order on rdma port (bz 1310691)
- blkmapd: Add the -h flag on the man page (bz 1001431)
- nfsd: Remove some warnings nfsd.c (bz 1336419)
- mountd.man: Update to change -P option as an alias for -p (bz 1037924)
- mountd: cleaned up usage message (bz 1003716)
- mountstats.man: fixed typo in man page (bz 1263966)

* Mon May 16 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.26
- gssd: use pthreads to handle upcalls (bz 1331540)
- gssd: Fix inner-loop variable reuse (bz 1334848)
- mount: run START_STATD fully as root (bz 1275082)
- lockd: added lockd.conf to set module parameters (bz 1264387)

* Tue May  3 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.25
- mountstats.man:  Remove a few bogus .R macros (bz 1266013)
- systemd: ensure nfs-config service is re-run as needed (bz 1331460)
- exportfs: Deal with path's trailing "/"  (bz 1276534)
- exportfs: replace one xlog(D_GENERAL) in host_canonname() (bz 1331801)
- exportfs: Fix buf size in test_export() dump() (bz 1243234)
- blkmapd: Added a usage routine (bz 1001431)
- rpc.idmapd: Added a usage routine (bz 1001438)

* Thu Apr 28 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.24
- rpcgssd: added upstream debugging support (bz 1273163)
- start-statd: start rpc.statd only once (bz 1300007)
- exportfs: Don't stop the server from coming up when exportfs fails (bz 1287468)
- Changed install permissions on /var/lib/nfs/rpc_pipefs (bz 1291514)
- nfs.sysconfig: added note about the default keytab needing to exist (bz 1292607)
- mount.nfs: skip server address resolution on remount (bz 1313550)
- nfs_connect_nb: handle EINTR during connection establishment (bz 1299003)
- statd: Update existing record if we rece SM_MON with new cookie (bz 1284576)
- nfsidmap: updated to add in two new features (bz 1290488)

* Thu Feb 11 2016 Steve Dickson <steved@redhat.com> 1.3.0-0.23
- Update to nfsdcltrack v2 schema (bz 1285097)
- mountd: print an error message when no versions are specified (bz 1003539)
- mountd: added missing arugment to usage string (bz 1003716)

* Thu Dec  3 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.22
- nfsidmap: Correct a failure to set key timeout values (bz 1161222)
- exportfs: Restore the EAI_NONAME check in host_pton() (bz 1276099)
- gssd: Don't assume the machine account will be in uppercase (bz 1268040)

* Tue Sep 29 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.21
- Stop gssd from flooding the KDC with TGT fetches (bz 1264999)
- Decouple the start/stop of rpcbind with nfs-server and rpc-statd (bz 1266993)

* Mon Sep 14 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.20
- Added back MOUNT_PORT (bz 1208488)
- rpc-statd now Requires rpcbind.service (bz 1171603)

* Thu Sep  3 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.19
- Removed the patch for bz1256469 (bz 1259771)

* Thu Aug 27 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.18
- Stop gssd from silenty reaps cache (bz 1256469)
- Remove errant echo call from spec file (bz 1257144)
- Add more symlinks to make systemd scripts backwards compatible (bz 1159183)

* Fri Jul 31 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.17
- Fixed return value being overrun in gssd (bz 1087350)

* Thu Jul 30 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.16
- Updated the mountstats-update.patch to include doc changes (bz 1215808)

* Thu Jul 23 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.15
- Make sure nfs-client target is enabled (bz 1245804)

* Tue Jul 14 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.14
- Fixed typeo in rpc.mount man page (bz 1003558)

* Wed Jul  1 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.13
- Fix infinite loop in blkmapd (bz 1237301)

* Wed Jun 24 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.12
- Fixed nfs-idmap start race (bz 1164064)
- Updated nfsdcltrack v2 schema (bz 1234598)
- Added missing arguments in rpc.mountd man page (bz 1003558)
- Added nfsconfig.conf to nfs.man and mount.nfs.man (bz 1196646)
- nfs-server now Requires rpcbind.service (bz 1171603)

* Thu Jun 11 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.11
- Added the rpcuser group before adding the rpcuser uid (bz 1190874)
- Added back variables to help get through firewalls (bz 1208488)
- Made the postuns conditional (bz 1200713)

* Mon May  4 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.10
- Updated mountstats to latest upstream version (bz 1215808)
- Enable all auth flavors on pseudofs exports (bz 1187223)

* Tue Apr 28 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.9
- Updates for block pNFS (bz 1214821)

* Fri Jan 23 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.8
- Stop sm-notify from running in HA environments (bz 1182692)
- Set the GSS_USE_PROXY variable in nfs-utils_env.sh (bz 1183821)

* Thu Jan 15 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.7
- rpc.idmapd now comes down with the nfs server (bz 1159234)

* Wed Jan  7 2015 Steve Dickson <steved@redhat.com> 1.3.0-0.6
- Corrected argument names in the systemd scripts (bz 1170364)
- Added RELRO check (bz 1092543)
- Properly parse IPv6 literal strings with null termination (bz 1161490)
- Added the 'nordirplus' export flag to disable v3 readdirplus (bz 1161458)

* Fri Nov 14 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.5
- Fixed a mound DOS (bz 1163891)

* Fri Oct 24 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.4
- Added verbosity back to umount (bz 923582)

* Wed Oct 15 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.3
- Enable gssproxy in /etc/sysconf/nfs (bz 1082746)

* Mon Sep 29 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.2
- Upgrade to latest upstream systemd scripts  (bz 1144440)
- Taught start-statd to use systemd  (bz 1144440)
- Repaced rpc.svcgssd with gssproxy (bz 1082746)

* Fri Sep 19 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.1
- Added configurable timeout to rpc.gssd (bz 1009528)
- Added callback to sm_notify (bz 1108105)
- mountd: Fixed path in start-statd (bz 1116794)
- rpc.gssd: Fixed silent error message (bz 1117384)
- rpc.gssd: add the acceptor name to the info passed in downcall (bz 1088011)
- nfs-utils.spec: fixed runtime configuration files (bz 1118177)
- exportfs: fix test of NULL pointer in host_pton() (bz 1083018)
- gssd: Fixed errno typo in get_servername() (bz 1082480)
- nfsiostat: documented the output better (bz 1109864)

* Wed Mar 26 2014 Steve Dickson <steved@redhat.com> 1.3.0-0.0
- Updated to latest upstream release: nfs-utils-1-3-0
  - mount.nfs: Fix fallback from tcp to udp (bz 984901)
  - nfsidmap: Keys need to be invalidated instead of revoked (bz 1080505)
- Removed RDMA_PORT stub from /etc/sysconfig/nfs (bz 1078792)

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1:1.2.9-4
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Steve Dickson <steved@redhat.com> 1.2.9-3.1
- gssd: set $HOME to prevent recursion when home dirs are on kerberized NFS mount (bz 1056658)

* Mon Jan 20 2014 Steve Dickson <steved@redhat.com> 1.2.9-3.0
- Updated to the latest upstream RC release nfs-utils-1.2.10-rc3
  - exportfs: Exit with correct value when an error occurs (bz 1053933)
  - mount.nfs: Removed supported flag from usage string (bz 1000989)
  - gssd: Improve first attempt at acquiring GSS credentials (bz 1053877)
  - rpc.idmapd: Remove no longer supported flags from man page (bz 1003513)
  - rpc.statd: Allow usage messages to be displayed when statd is running. (bz 1037044)

* Wed Jan  8 2014 Steve Dickson <steved@redhat.com> 1.2.9-2.1
- exportfs: Remove a buffer overlow (bz 1008384)
- nfs-server: Added an Also cause (bz 1050161)

* Wed Jan  8 2014 Steve Dickson <steved@redhat.com> 1.2.9-2.0
- Updated to the latest upstream RC release nfs-utils-1.2.10-rc2
  - mount.nfs: Eliminated long delays during mount (bz 1031643)
  - exportfs: Corrected erroneously error messages (bz 1049589)

* Tue Jan  7 2014 Steve Dickson <steved@redhat.com> 1.2.9-0.5
- Reverted patch for bz1029573. The kernel can now detect 
  when rpc.gssd is or is not running (bz1031197)
- gssd: always reply to rpc-pipe requests from kernel. (bz1031197)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.2.9-0.4
- Mass rebuild 2013-12-27

* Tue Nov 12 2013 Steve Dickson <steved@redhat.com> 1.2.9-0.3
- The patch for bz 1029573 had a zero length due a typo (bz 1029573)

* Tue Nov 12 2013 Steve Dickson <steved@redhat.com> 1.2.9-0.2 
- gssd will return immediately when a keytab is not readable (bz 1029573)

* Thu Nov 7 2013 Steve Dickson <steved@redhat.com> 1.2.9-0.1
- Reordered how mountd and nfsd are started (bz 963138)

* Tue Nov 5 2013 Steve Dickson <steved@redhat.com> 1.2.9-0.0
- Updated to latest upstream Release: nfs-utils-1-2-9
- Fixed a mounting error (bz 963580)

* Thu Aug 22 2013 Steve Dickson <steved@redhat.com> 1.2.8-4.1
- nfs-utils: fix a number of specfile problems

* Mon Aug 19 2013 Steve Dickson <steved@redhat.com> 1.2.8-4.0
- Updated to latest upstream RC release: nfs-utils-1-2-9-rc4

* Tue Jul 23 2013 Steve Dickson <steved@redhat.com> 1.2.8-3.0
- Updated to latest upstream RC release: nfs-utils-1-2-9-rc3

* Tue Jul 23 2013 Steve Dickson <steved@redhat.com> 1.2.8-2.1
- Make sure nfs.target is enabled (bz 970595)
- Fix nfs server reloads (bz 951247)

* Fri May 31 2013 Steve Dickson <steved@redhat.com> 1.2.8-2.0
- Update to latest upstream RC release: nfs-utils.1.2.9-rc1
- Added GSS_USE_PROXY variable to nfs.sysconfig (bz 967112)

* Tue May  7 2013 Steve Dickson <steved@redhat.com> 1.2.8-1.1
  systemd: nfs-server.service needs to be split up (bz 769879)

* Tue May  7 2013 Steve Dickson <steved@redhat.com> 1.2.8-1
- Updated to the latest upstream RC release: nfs-utils.1.2.9-rc1

* Tue Apr 23 2013 Steve Dickson <steved@redhat.com> 1.2.8-0
- Updated to latest upstream release: 1.2.8
- Removed the libgssglue dependency

* Mon Apr  1 2013 Steve Dickson <steved@redhat.com> 1.2.7-6
- Added v4.1 support rpc.nfsd (bz 947073)

* Mon Mar 25 2013 Steve Dickson <steved@redhat.com> 1.2.7-5
- Updated to latest upstream RC release: nfs-utils.1.2.8-rc4
- Added nfs-lock.service to After line in nfs-server.service (bz 914792)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Steve Dickson <steved@redhat.com> 1.2.7-3
- Updated to latest upstream RC release: nfs-utils.1.2.8-rc3
- Took ownership of /usr/lib/nfs-utils (bz 894535)

* Mon Dec 17 2012 Steve Dickson <steved@redhat.com> 1.2.7-2
- Update to latest upstream RC release: nfs-utils.1.2.8-rc2

* Wed Nov 28 2012 Steve Dickson <steved@redhat.com> 1.2.7-1
- Update to latest upstream RC release: nfs-utils.1.2.8-rc1

* Fri Nov  9 2012 Steve Dickson <steved@redhat.com> 1.2.7-0
- Updated to latest upstream release: nfs-utils.1.2.7

* Thu Nov  8 2012 Steve Dickson <steved@redhat.com> 1.2.6-14
- Allow the service to start when RPCNFSDCOUNT is comment out. (bz 870143)
- Removed some old cruft from the spec file (bz 226198)

* Mon Oct 15 2012 Steve Dickson <steved@redhat.com> 1.2.6-13
- Added a Requires for the quota package (bz 866225)

* Thu Aug 23 2012 Steve Dickson <steved@redhat.com> 1.2.6-12 
- Added FedFS support by added a BuildRequires for fedfs-utils-devel
- Introduce new systemd-rpm macros (bz 850227)
- Updated to latest upstream RC release: nfs-utils.1.2.7-rc5 (bz 833024)

* Mon Aug  6 2012 Steve Dickson <steved@redhat.com> 1.2.6-11
- Updated to latest upstream RC release: nfs-utils.1.2.7-rc4

* Thu Aug  2 2012 Steve Dickson <steved@redhat.com> 1.2.6-10
- Removed modprobe.d/nfs.conf 

* Thu Jul 19 2012 Steve Dickson <steved@redhat.com> 1.2.6-9
- Updated to latest upstream RC release: nfs-utils.1.2.7-rc3

* Thu Jul  5 2012 Steve Dickson <steved@redhat.com> 1.2.6-8
- nfsidmap: default domain no being set (bz 829362)

* Fri Jun 22 2012 Steve Dickson <steved@redhat.com> 1.2.6-7
- Reworked how the legacy names are enabled in systemd
- Fixed typo in nfs-mountd.service

* Tue Jun 12 2012 Steve Dickson <steved@redhat.com> 1.2.6-6
- Updated to latest upstream RC release: nfs-utils.1.2.7-rc2 (bz 833555)

* Tue Jun 12 2012 Steve Dickson <steved@redhat.com> 1.2.6-5
- Reworked how the services are restarted.

* Tue Jun 12 2012 Steve Dickson <steved@redhat.com> 1.2.6-4
- Enable legacy service names.

* Tue May 29 2012 Steve Dickson <steved@redhat.com> 1.2.6-3
- Updated to latest upstream RC release: nfs-utils.1.2.7-rc1

* Tue May 29 2012 Steve Dickson <steved@redhat.com> 1.2.6-2
* Fixed typo in the checking of nfsnobody (bz 816149)

* Fri May 25 2012 Steve Dickson <steved@redhat.com> 1.2.6-1
- Correctly search for the existence of nfsnobody (bz 816149)
- Correctly change the default group id for nfsnobody (bz 816149)

* Tue May 15 2012 Steve Dickson <steved@redhat.com> 1.2.6-0
- Update to the latest upstream release: nfs-utils-1.2.6 (bz 821673)
- Split out NFS server daemons into individual service files (bz 769879) 
- Removed Wants= from nfs-lock.service (bz 817895)
- Only enable services if they are enabled on upgrades (bz 807020)

* Thu May  3 2012 Steve Dickson <steved@redhat.com> 1.2.5-16
- Update to the latest RC release: nfs-utils-1.2.6-rc7

* Thu Apr 26 2012 Josh Boyer <jwboyer@redhat.com> 1.2.5-15
- Add modprobe config file to alias 'nfs4' to 'nfs' (bz 806333)

* Thu Mar 22 2012 Steve Dickson <steved@redhat.com> 1.2.5-14
- gssd: Look for user creds in user defined directory (bz 786993)
- gssd: Don't link with libgssapi_krb5 (bz 784908)

* Fri Mar 16 2012 Steve Dickson <steved@redhat.com> 1.2.5-13
- Make sure statd is start before NFS mounts (bz 786050)
- rpc.idmap: Hide global symbols from libidmap plugins (bz 797332)
- nfsd: Bump up the default to 8 nprocs (bz 757452)

* Wed Feb 08 2012 Harald Hoyer <harald@redhat.com> 1.2.5-12
- require kmod instead of modutils (bz 788571)

* Mon Jan 16 2012 Steve Dickson <steved@redhat.com> 1.2.5-11
- Update to upstream RC release: nfs-utils-1.2.6-rc6
- Reworked how the nfsd service requires the rpcbind service (bz 768550)

* Mon Jan  9 2012 Steve Dickson <steved@redhat.com> 1.2.5-10
- Added back the SUID bits on mount commands (bz 772396)
- Added a decency on keyutils (bz 769724)

* Thu Jan  5 2012 Steve Dickson <steved@redhat.com> 1.2.5-9
- Update to upstream RC release: nfs-utils-1.2.6-rc5

* Thu Dec 15 2011 Steve Dickson <steved@redhat.com> 1.2.5-8
- Removed the nfs-idmap service. rpc.idmap is now part of
  the nfs-server service

* Tue Dec 13 2011 Steve Dickson <steved@redhat.com> 1.2.5-7
- Enabled new idmaping by installing the id_resolver.conf file.
- Update to upstream RC release: nfs-utils-1.2.6-rc4

* Fri Nov 18 2011 Steve Dickson <steved@redhat.com> 1.2.5-6
- Remove RQUOTAD_PORT and RQUOTAD from /etc/sysconfig/nfs (bz 754496)
- Ensured nfs-idmap service is started after the named is up (bz 748275)

* Mon Nov 14 2011 Steve Dickson <steved@redhat.com> 1.2.5-5
- Ensured nfs-idmap service is started after the network up (bz 748275)
- Update to upstream RC release: nfs-utils-1.2.6-rc3 (bz 746497)

* Thu Oct 20 2011 Steve Dickson <steved@redhat.com> 1.2.5-4
- Added pNFS debugging to rpcdebug.

* Tue Oct 18 2011 Steve Dickson <steved@redhat.com> 1.2.5-3
- Update to upstream RC release: nfs-utils-1.2.6-rc2

* Tue Oct  4 2011 Steve Dickson <steved@redhat.com> 1.2.5-2
- Removed SUID bits on mount commands (bz 528498)
- Fixed a few typos in a couple man pages (bz 668124, 673818, 664330)
- Fixed a I/0 problem in rpc.idmapd (bz 684308)

* Mon Oct  3 2011 Steve Dickson <steved@redhat.com> 1.2.5-1
- Update to upstream RC release: nfs-utils-1.2.6-rc1
- Added named.service to After list in nfs-server.service (bz 742746)

* Tue Sep 27 2011 Steve Dickson <steved@redhat.com> 1.2.5-0
- Update to upstream release: nfs-utils-1.2.5 (bz 717931)

* Wed Sep 21 2011 Steve Dickson <steved@redhat.com> 1.2.4-11
- Update to upstream RC release: nfs-utils-1.2.5-rc3

* Wed Sep 14 2011 Steve Dickson <steved@redhat.com> 1.2.4-10
- Created /etc/exports.d to stop a warning (bz 697006)

* Tue Aug 30 2011 Steve Dickson <steved@redhat.com> 1.2.4-9
- Both the nfs.lock and nfs.idmap services should always
  enabled on both installs and upgrades (bz 699040)
- Fixed the paths to the server scriptlets (bz 733531)

* Mon Aug 29 2011 Steve Dickson <steved@redhat.com> 1.2.4-8
- Update to upstream RC release: nfs-utils-1.2.5-rc2

* Wed Aug 24 2011 Steve Dickson <steved@redhat.com> 1.2.4-7
- Added StandardError=syslog+console to all the service files
  so startup errors will be logged. 
- Changed exportfs to only log errors on existing /etc/export.d 
  directory, which eliminates a needless syslog entry.
- Automount /proc/fs/nfsd for rpc.nfsd 

* Wed Aug 10 2011 Steve Dickson <steved@redhat.com> 1.2.4-6
- Fixed some bugs in the triggerun script as well in
  the nfs-server scripts (bz 699040).

* Wed Aug  3 2011 Steve Dickson <steved@redhat.com> 1.2.4-5
- Cleaned up the .preconfig and .postconfig files per
  code review request.

* Wed Aug  3 2011 Steve Dickson <steved@redhat.com> 1.2.4-4
- Converted init scrips to systemd services. (bz 699040)
- Made nfsnobody's uid/gid to always be a 16-bit value of -2
- mount: fix for libmount from util-linux >= 2.20

* Thu Jul 21 2011 Steve Dickson <steved@redhat.com> 1.2.4-3
- Updated to latest upstream release: nfs-utils-1-2-5-rc1

* Thu Jul  7 2011 Ville Skyttä <ville.skytta@iki.fi> - 1:1.2.4-2
- Don't ship Makefiles or INSTALL in docs (#633934).

* Mon Jul  4 2011 J. Bruce Fields <bfields@redhat.com> 1.2.4-1
- Rely on crypto module autoloading in init scripts
- initscripts: just try to mount rpc_pipefs always

* Wed Jun 29 2011 Steve Dickson <steved@redhat.com> 1.2.4-0
- Updated to latest upstream release: nfs-utils-1-2-4

* Wed Apr 20 2011 Steve Dickson <steved@redhat.com> 1.2.3-13
- Updated to latest upstream release: nfs-utils-1-2-4-rc8

* Wed Apr  6 2011 Steve Dickson <steved@redhat.com> 1.2.3-12
- Updated to latest upstream release: nfs-utils-1-2-4-rc7
- Enabled the libmount code.

* Mon Mar  7 2011 Steve Dickson <steved@redhat.com> 1.2.3-11
- Updated to latest upstream release: nfs-utils-1-2-4-rc6

* Wed Feb 09 2011 Christopher Aillon <caillon@redhat.com> - 1.2.3-10
- Rebuild against newer libevent

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Steve Dickson <steved@redhat.com> 1.2.3-8
- Fixed segfault in rpc.mountd (bz 669065)

* Fri Jan 14 2011 Steve Dickson <steved@redhat.com> 1.2.3-7
- Updated to latest upstream release: nfs-utils-1-2-4-rc5
- Add initscripts changes needed for rpcbind to be running when nfs is started
- Initscripts changes needed to support NFS over RDMA
- Allow the setting of the NFSv4 grace period (bz 665387)

* Mon Dec 13 2010 Steve Dickson <steved@redhat.com> 1.2.3-6
- Updated to latest upstream release: nfs-utils-1-2-4-rc4

* Wed Dec  8  2010 Steve Dickson <steved@redhat.com> 1.2.3-5
- Replace the nfs-utils-lib dependency with a libnfsidmap 
  dependency

* Wed Dec  1  2010 Steve Dickson <steved@redhat.com> 1.2.3-4
- The nfs service is not stopped on reboot or halt (bz 652786)
- Removed obsolete configuration values (bz 653765)

* Mon Nov 29 2010 Steve Dickson <steved@redhat.com> 1.2.3-3
- Updated to latest upstream release: nfs-utils-1-2-4-rc3

* Fri Oct 15 2010 Steve Dickson <steved@redhat.com> 1.2.3-2
- Initscripts do not conform to LSB specification (bz 621562)
- sm-notify needs to call res_init() before each try (bz 625531)
- exports(5) man page duplicated paragraphs (bz 590921)

* Thu Oct 14 2010 Steve Dickson <steved@redhat.com> 1.2.3-1
- Updated to latest upstream release: nfs-utils-1-2-4-rc1

* Mon Oct  4 2010 Steve Dickson <steved@redhat.com> 1.2.3-0.1
- Fixed a regession with -p arguemnt to rpc.mountd 

* Thu Sep 30 2010 Steve Dickson <steved@redhat.com> 1.2.3-0
- Updated to latest upstream release: nfs-utils-1-2-3

* Thu Sep 16 2010 Steve Dickson <steved@redhat.com> 1.2.2-8
- Update to upstream RC release: nfs-utils-1-2-3-rc6

* Thu Sep  9 2010 Steve Dickson <steved@redhat.com> 1.2.2-7
- Update to upstream RC release: nfs-utils-1-2-3-rc5

* Tue Jun 22 2010 Steve Dickson <steved@redhat.com> 1.2.2-6
- Update to upstream RC release: nfs-utils-1-2-3-rc4

* Thu May  6 2010 Steve Dickson <steved@redhat.com> 1.2.2-4
- Update to upstream RC release: nfs-utils-1-2-3-rc3

* Fri Apr 16 2010 Steve Dickson <steved@redhat.com> 1.2.2-3
- Update to upstream RC release: nfs-utils-1-2-3-rc2

* Mon Mar 22 2010 Steve Dickson <steved@redhat.com> 1.2.2-2
- Update to upstream RC release: nfs-utils-1-2-3-rc1

* Thu Feb 18 2010 Steve Dickson <steved@redhat.com> 1.2.2-1
- Updated to latest upstream version: 1.2.2

* Thu Jan 28 2010 Steve Dickson <steved@redhat.com> 1.2.1-17
- Backed out the  "Don't fail mounts when /etc/netconfig is 
  nonexistent" patch

* Wed Jan 27 2010 Steve Dickson <steved@redhat.com> 1.2.1-16
- mount.nfs: Don't fail mounts when /etc/netconfig is nonexistent

* Mon Jan 25 2010 Steve Dickson <steved@redhat.com> 1.2.1-15
- statd: Teach nfs_compare_sockaddr() to handle NULL 
  arguments

* Fri Jan 22 2010 Steve Dickson <steved@redhat.com> 1.2.1-14
- Update to upstream RC release: nfs-utils-1-2-2-rc9

* Thu Jan 21 2010 Steve Dickson <steved@redhat.com> 1.2.1-13
- mount.nfs: Configuration file parser ignoring options
- mount.nfs: Set the default family for lookups based on 
    defaultproto= setting
- Enabled ipv6 

* Sun Jan 17 2010 Steve Dickson <steved@redhat.com> 1.2.1-12
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc7
  which includes Ipv6 support for tcpwrapper (disabled by default).

* Sat Jan 16 2010 Steve Dickson <steved@redhat.com> 1.2.1-11
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc7
  which includes Ipv6 support for statd (disabled by default).

* Thu Jan 14 2010 Steve Dickson <steved@redhat.com> 1.2.1-10
- Updated to the latest pseudo root release (rel10) which
  containts the upstream pseudo root release

* Tue Jan 12 2010 Steve Dickson <steved@redhat.com> 1.2.1-9
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc5

* Mon Jan  4 2010 Steve Dickson <steved@redhat.com> 1.2.1-8
- mount.nfs: don't use IPv6 unless IPV6_SUPPORTED is set

* Mon Dec 14 2009 Steve Dickson <steved@redhat.com> 1.2.1-7
- Updated to latest upstream RC release: nfs-utils-1-2-2-rc3

* Thu Dec 10 2009 Steve Dickson <steved@redhat.com> 1.2.1-6
- Update the  pseudo root to handle security flavors better.

* Mon Dec  7 2009 Steve Dickson <steved@redhat.com> 1.2.1-5
- mount.nfs: Retry v4 mounts with v3 on ENOENT errors

* Mon Dec  7 2009 Steve Dickson <steved@redhat.com> 1.2.1-4
- Updated to the latest pseudo root release (rel9) (bz 538609).

* Thu Nov 12 2009 Steve Dickson <steved@redhat.com> 1.2.1-3
- Stop rpc.nfsd from failing to startup when the network
  is down (bz 532270)

* Wed Nov 11 2009 Steve Dickson <steved@redhat.com> 1.2.1-2
- Updated to the latest pseudo root release (rel8).

* Wed Nov 4 2009 Steve Dickson <steved@redhat.com> 1.2.1-1
- Updated to latest upstream release: 1.2.0

* Tue Nov 3 2009 Steve Dickson <steved@redhat.com> 1.2.0-18
- Reworked and remove some of the Default-Start/Stop stanzas
  in the init scripts (bz 531425)

* Mon Nov 2 2009 Steve Dickson <steved@redhat.com> 1.2.0-17
- Updated to the latest pseudo root release (rel7).
- Added upstream 1.2.1-rc7 patch which fixes:
  - Stop ignoring the -o v4 option (bz 529407)
  - Allow network protocol roll backs when proto is set
    in the config file (bz 529864)
- v4 mounts will roll back to v3 mounts when the mount
  fails with ENOENT. 

* Mon Oct  5 2009 Steve Dickson <steved@redhat.com> 1.2.0-16
- Fixed a whole where '-o v4' was not overriding the
  version in the conf file.

* Wed Sep 30 2009 Steve Dickson <steved@redhat.com> 1.2.0-15
- Change the nfsmount.conf file to define v3 as the default 
  protocol version.
- Make sure versions set on the command line override version
  set in nfsmount.conf
- Make version rollbacks still work when versions are set in
  nfsmount.conf

* Tue Sep 29 2009 Steve Dickson <steved@redhat.com> 1.2.0-13
- Added upstream 1.2.1-rc5 patch
  - mount.nfs: Support negotiation between v4, v3, and v2
  - mount.nfs: Keep server's address in nfsmount_info
  - mount.nfs: Sandbox each mount attempt
  - mount.nfs: Support negotiation between v4, v3, and v2

* Wed Sep 23 2009 Steve Dickson <steved@redhat.com> 1.2.0-12
- Updated to the latest pseudo root release (rel6).

* Tue Sep 15 2009 Steve Dickson <steved@redhat.com> 1.2.0-11
- Added upstream 1.2.1-rc5 patch
  - Added --sort --list functionality to nfs-iostat.py
  - Fixed event handler in idmapd
  - Added -o v4 support
  - Disabled IPv6 support in nfsd
  - Don't give client an empty flavor list
  - Fixed gssed so it does not blindly caches machine credentials

* Mon Aug 17 2009 Steve Dickson <steved@redhat.com> 1.2.0-10
- Added upstream 1.2.1-rc4 patch
  - Fix bug when both crossmnt
  - nfs(5): Add description of lookupcache mount option
  - nfs(5): Remove trailing blanks
  - Added nfs41 support to nfssat
  - Added support for mount to us a configuration file.

* Fri Aug 14 2009 Steve Dickson <steved@redhat.com> 1.2.0-9
- Added upstream 1.2.1-rc3 patch
  - Add IPv6 support to nfsd
  - Allow nfssvc_setfds to properly deal with AF_INET6
  - Convert nfssvc_setfds to use getaddrinfo
  - Move check for active knfsd to helper function
  - Declare a static common buffer for nfssvc.c routine
  - Convert rpc.nfsd to use xlog() and add --debug and --syslog options

* Tue Jul 28 2009 Steve Dickson <steved@redhat.com> 1.2.0-8
- Fixed 4.1 versioning problem (bz 512377)

* Wed Jul 15 2009 Steve Dickson <steved@redhat.com> 1.2.0-7
- Added upstream 1.2.1-rc2 patch
  - A large number of mount command changes.

* Mon Jul 13 2009 Steve Dickson <steved@redhat.com> 1.2.0-6
- Added NFSD v4 dynamic pseudo root patch which allows
  NFS v3 exports to be mounted by v4 clients.

* Mon Jun 29 2009 Steve Dickson <steved@redhat.com> 1.2.0-5
- Stopped rpc.idmapd from spinning (bz 508221)

* Mon Jun 22 2009 Steve Dickson <steved@redhat.com> 1.2.0-4
- Added upstream 1.2.1-rc1 patch 
  - Fix to check in closeall()
  - Make --enable-tirpc the default
  - Set all verbose types in gssd daemons
  - Retry exports if getfh() fails

* Wed Jun 10 2009 Steve Dickson <steved@redhat.com> 1.2.0-3
- Updated init scripts to add dependencies
  on other system facilities (bz 475133)

* Wed Jun 10 2009 Steve Dickson <steved@redhat.com> 1.2.0-2
- nfsnobody gid is wrong (bz 485379)

* Tue Jun  2 2009 Steve Dickson <steved@redhat.com> 1.2.0-1
- Updated to latest upstream release: 1.2.0

* Tue May 19 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.6-4
- Replace the Sun RPC license with the BSD license, with the explicit permission of Sun Microsystems

* Mon May 18 2009 Steve Dickson <steved@redhat.com> 1.1.6-3
- Added upstream 1.1.7-rc1 patch 
  - utils/nfsd: add support for minorvers4
  - sm-notify: Don't orphan addrinfo structs
  - sm-notify: Failed DNS lookups should be retried
  - mount: remove legacy version of nfs_name_to_address()
  - compiling error in rpcgen
  - nfs-utils: Fix IPv6 support in support/nfs/rpc_socket.c
  - umount.nfs: Harden umount.nfs error reportin

* Mon Apr 27 2009 Steve Dickson <steved@redhat.com> 1.1.6-2
- nfslock.init: options not correctly parsed (bz 459591)

* Mon Apr 20 2009 Steve Dickson <steved@redhat.com> 1.1.6-1
- Updated to latest upstream release: 1.1.6

* Mon Mar 23 2009 Steve Dickson <steved@redhat.com> 1.1.5-4
- Added upstream rc3 patch
  - gssd: initialize fakeseed in prepare_krb5_rfc1964_buffer
  - gssd: NULL-terminate buffer after read in read_service_info (try #2)
  - gssd: free buffer allocated by gssd_k5_err_msg
  - gssd: fix potential double-frees in gssd
  - Removed a number of warn_unused_result warnings

* Mon Mar 16 2009 Steve Dickson <steved@redhat.com> 1.1.5-3
- Added upstream rc2 patch

* Fri Mar  6 2009 Steve Dickson <steved@redhat.com> 1.1.5-2
- Fixed lockd not using settings in sysconfig/nfs (bz 461043)
- Fixed some lost externs in the tcpwrapper code

* Thu Mar  5 2009 Steve Dickson <steved@redhat.com> 1.1.5-1
- Updated to latest upstream version: 1.1.5

* Wed Mar  4 2009 Steve Dickson <steved@redhat.com> 1.1.4-21
- configure: fix AC_CACHE_VAL warnings

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Steve Dickson <steved@redhat.com> 1.1.4-19
- Exportfs and rpc.mountd optimalization (bz 76643)

* Tue Feb 17 2009 Steve Dickson <steved@redhat.com> 1.1.4-18
- umount.nfs command: Add an AF_INET6-capable version of nfs_call_unmount()
- umount.nfs command: Support AF_INET6 server addresses
- umount command: remove do_nfs_umount23 function

* Tue Feb 17 2009 Steve Dickson <steved@redhat.com> 1.1.4-17
- Integrated the upstream fix for bz 483375
- mount: segmentation faults on UDP mounts (bz 485448)

* Sat Jan 31 2009 Steve Dickson <steved@redhat.com> 1.1.4-16
- Fixed typo in -mount-textbased.patch (bz 483375)

* Sat Jan 31 2009 Steve Dickson <steved@redhat.com> 1.1.4-15
- Reworked tcp wrapper code to correctly use API (bz 480223)
- General clean up of tcp wrapper code.

* Tue Jan 27 2009 Steve Dickson <steved@redhat.com> 1.1.4-14
- text-based mount command: make po_rightmost() work for N options
- text-based mount command: Function to stuff "struct pmap" from mount options
- text-based mount options: Use new pmap stuffer when	rewriting mount options
- text-based mount command: fix mount option rewriting logic
- text-based mount command: support AF_INET6 in rewrite_mount_options()

* Tue Jan 20 2009 Steve Dickson <steved@redhat.com> 1.1.4-13
- mountd: Don't do tcp wrapper check when there are no rules (bz 448898)

* Wed Jan  7 2009 Steve Dickson <steved@redhat.com> 1.1.4-12
- configure: Remove inet_ntop(3) check from configure.ac
- configure: Add new build option "--enable-tirpc"
- showmount command: Quiesce warning when TI-RPC is disabled

* Sat Jan  3 2009 Steve Dickson <steved@redhat.com> 1.1.4-11
- Added warnings to tcp wrapper code when mounts are 
  denied due to misconfigured DNS configurations.
- gssd: By default, don't spam syslog when users' credentials expire
- mount: revert recent fix for build problems on old systems
- mount: use gethostbyname(3) when building on old systems
- mount: getport: don't use getaddrinfo(3) on old systems
- mount: Random clean up
- configure: use "--disable-uuid" instead of	"--without-uuid"

* Fri Dec 19 2008 Steve Dickson <steved@redhat.com> 1.1.4-10
- Re-enabled and fixed/enhanced tcp wrappers.

* Wed Dec 17 2008 Steve Dickson <steved@redhat.com> 1.1.4-9
- text-based mount command: add function to parse numeric mount options
- text-based mount command: use po_get_numeric() for handling retry
- sm-notify command: fix a use-after-free bug
- statd: not unlinking host files

* Thu Dec 11 2008 Steve Dickson <steved@redhat.com> 1.1.4-8
- mount command: AF_INET6 support for probe_bothports()
- mount command: support AF_INET6 in probe_nfsport() and probe_mntport()
- mount command: full support for AF_INET6 addresses in probe_port()
- gssd/svcgssd: add support to retrieve actual context expiration
- svcgssd: use the actual context expiration for cache

* Sat Dec  6 2008 Steve Dickson <steved@redhat.com> 1.1.4-7
- sm-notify: always exiting without any notification.

* Tue Dec  2 2008 Steve Dickson <steved@redhat.com> 1.1.4-6
- mount command: remove local getport() implementation
- mount command: Replace clnt_ping() and getport() calls in probe_port()
- mount command: Use nfs_error() instead of perror()
- mount command: Use nfs_pmap_getport() in probe_statd()

* Mon Dec  1 2008 Steve Dickson <steved@redhat.com> 1.1.4-5
- Make sure /proc/fs/nfsd exists when the nfs init script
  does the exports (bz 473396)
- Fixed typo in nfs init script that caused rpc.rquotad daemons
  to be started but not stoppped (bz 473929)

* Wed Nov 26 2008 Steve Dickson <steved@redhat.com> 1.1.4-4
- gssd: unblock DNOTIFY_SIGNAL in case it was blocked
- Ensure statd gets started if required when non-root
  user mounts an NFS filesystem

* Tue Nov 25 2008 Steve Dickson <steved@redhat.com> 1.1.4-3
- Give showmount support for querying via rpcbindv3/v4 

* Tue Nov 18 2008 Steve Dickson <steved@redhat.com> 1.1.4-2
- Add AF_INET6-capable API to acquire an RPC CLIENT
- Introduce rpcbind client utility functions

* Sat Oct 18 2008 Steve Dickson <steved@redhat.com> 1.1.4-1
- Updated to latest upstream version: 1.1.4

* Tue Oct 14 2008 Steve Dickson <steved@redhat.com> 1.1.3-6
- sm-notify exists when there are no hosts to notify

* Thu Sep 18 2008 Steve Dickson <steved@redhat.com> 1.1.3-5
- Reworked init scripts so service will be able to
  stop when some of the checks fail. (bz 462508)
- Pre-load nfsd when args to rpc.nfsd are given (bz 441983)

* Thu Aug 28 2008 Steve Dickson <steved@redhat.com> 1.1.3-4
- Added in a number of up upstream patches (101 thru 110).

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.3-3
- fix license tag

* Thu Jul 31 2008 Steve Dickson <steved@redhat.com> 1.1.3-2
- Mount command did not compile against older glibc versions.

* Mon Jul 28 2008 Steve Dickson <steved@redhat.com> 1.1.3-1
- Updated to latest upstream version: 1.1.3

* Wed Jul  2 2008 Steve Dickson <steved@redhat.com> 1.1.2-12
- Changed the default directories for sm-notify (bz 435480)
- Added 'condstop' to init scripts so service are not
  started when nfs-utils is removed.

* Mon Jun 30 2008 Dennis Gilmore <dennis@ausil.us> 1.1.2-11
- add sparc arch handling 

* Mon Jun 30 2008 Steve Dickson <steved@redhat.com>  1.1.2-10
- Rebuild for the updated libevent lib.

* Fri Jun 27 2008 Steve Dickson <steved@redhat.com>  1.1.2-9
- Removed the nfslock service start/stop from %%post section 
  (bz 453046)

* Wed Jun 25 2008 Steve Dickson <steved@redhat.com>  1.1.2-8
- FQDNs in the rmtab causes exportfs to seg fault (bz 444275)

* Mon Jun 23 2008 Steve Dickson <steved@redhat.com>  1.1.2-7
- Added -D_FILE_OFFSET_BITS=64 to CFLAGS
- make nfsstat read and print stats as unsigned integers
- Added (but not installed) the mountstats and nfs-iostat
  python scripts.

* Fri Jun  6 2008 Steve Dickson <steved@redhat.com>  1.1.2-6
- Added 5 (111 thru 115) upstream patches that fixed
  things mostly in the text mounting code.

* Thu May  8 2008 Steve Dickson <steved@redhat.com>  1.1.2-5
- Added 10 (101 thru 110) upstream patches that fixed
  things mostly in the mount and gssd code.

* Wed May  7 2008 Steve Dickson <steved@redhat.com>  1.1.2-4
- Added ppc arch to the all_32bit_archs list (bz 442847)

* Wed Apr 23 2008 Steve Dickson <steved@redhat.com>  1.1.2-3
- Documented how to turn off/on protocol support for
  rpc.nfsd in /etc/sysconfig/nfs (bz443625)
- Corrected the nfslock initscript 'status' return code (bz 441605)
- Removed obsolete code from the nfslock initscript (bz 441604)

* Mon Apr 14 2008 Steve Dickson <steved@redhat.com>  1.1.2-2
- Make EACCES a non fatal error (bz 439807)

* Tue Mar 25 2008 Steve Dickson <steved@redhat.com>  1.1.2-1
- Upgrade to nfs-utils-1.1.2

* Mon Mar  3 2008 Steve Dickson <steved@redhat.com>  1.1.1-5
- Stopped mountd from incorrectly logging an error
  (commit 9dd9b68c4c44f0d9102eb85ee2fa36a8b7f638e3)
- Stop gssd from ignoring the machine credential caches
  (commit 46d439b17f22216ce8f9257a982c6ade5d1c5931)
- Fixed typo in the nfsstat command line arugments.
  (commit acf95d32a44fd8357c24e8a04ec53fc6900bfc58)
- Added test to stop buffer overflow in idmapd
  (commit bcd0fcaf0966c546da5043be700587f73174ae25)

* Sat Feb  9 2008 Steve Dickson <steved@redhat.com>  1.1.1-4
- Cleaned up some typos that were found in the various
  places in the mountd code

* Thu Jan 24 2008 Steve Dickson <steved@redhat.com>  1.1.1-3
- Added in relatime mount option so mount.nfs stays
  compatible with the mount command in util-linux-ng (bz 274301)

* Tue Jan 22 2008 Steve Dickson <steved@redhat.com>  1.1.1-2
- Added -S/--since to the nfsstat(1) manpage
- The wording in the exportfs man page can be a bit confusing, implying
  that "exportfs -u :/foo" will unexport /foo from all hosts, which it won't
- Removed nfsprog option since the kernel no longer supports it.
- Removed mountprog option since the kernel no longer supports it.
- Stop segfaults on amd64 during warnings messages.
- Fix bug when both crossmnt and fsid are set.

* Sat Jan  5 2008 Steve Dickson <steved@redhat.com>  1.1.1-1
- Updated to latest upstream release, nfs-utils-1.1.1
- Added the removal of sm-notify.pid to nfslock init script.
- Changed spec file to use condrestart instead of condstop
  when calling init scripts.
- Fixed typo in rpc.mountd man page 
- Turn on 'nohide' automatically for all refer exports (bz 313561)

* Tue Dec 04 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.1.0-7
 - Rebuild for openldap bump

* Wed Oct 17 2007 Steve Dickson <steved@redhat.com>  1.1.0-6
- Switch the libgssapi dependency to libgssglue

* Fri Sep 14 2007 Steve Dickson <steved@redhat.com>  1.1.0-5
- Changed the default paths in sm-notify to 
  /var/lib/nfs/statd (bz 258461)
- Updated exportfs manpage (bz 262861)

* Wed Aug 15 2007 Steve Dickson <steved@redhat.com>  1.1.0-4
- Make sure the open() system calling in exportfs uses
  mode bits when creating the etab file (bz 252440).

* Mon Aug 13 2007 Steve Dickson <steved@redhat.com>  1.1.0-3
- Added nosharecache mount option which re-enables
  rw/ro mounts to the same server (bz 243913).

* Thu Aug  2 2007 Steve Dickson <steved@redhat.com>  1.1.0-2
- Make sure the gss and idmap daemons remove thier lock
  files when they are stopped.

* Sat Jul 28 2007 Steve Dickson <steved@redhat.com>  1.1.0-1
- Upgraded to the latest upstream version (nfs-utils-1.1.0)

* Thu May 24 2007 Steve Dickson <steved@redhat.com> 1.0.10-7
- Fixed typo in mount.nfs4 that causes a segfault during
  error processing (bz 241190)

* Tue May 22 2007 Steve Dickson <steved@redhat.com> 1.0.10-6
- Make sure the condrestarts exit with a zero value (bz 240225)
- Stopped /etc/sysconfig/nfs from being overwritten on updates (bz 234543)
- Added -o nordirplus mount option to disable READDIRPLUS (bz 240357)
- Disabled the FSCache patch, for now... 

* Thu May 10 2007 Steve Dickson <steved@redhat.com> 1.0.12-5
- Fix mount.nfs4 to display correct error message (bz 227212)
- Updated mountd and showmount reverse lookup flags (bz 220772)
- Eliminate timeout on nfsd shutdowns (bz 222001)
- Eliminate memory leak in mountd (bz 239536)
- Make sure statd uses correct uid/gid by chowning
  the /var/lib/nfs/statd with the rpcuser id. (bz 235216)
- Correct some sanity checking in rpc.nfsd. (bz 220887) 
- Added missing unlock_mtab() call in moutnd
- Have mountd hold open etab file to force inode number to change (bz 236823)
- Create a /etc/sysconfig/nfs with all the possible init script
  variables (bz 234543)
- Changed nfs initscript to exit with correct value (bz 221874)

* Tue Apr  3 2007 Steve Dickson <steved@redhat.com> 1.0.12-4
- Replace portmap dependency with an rpcbind dependency (bz 228894)

* Mon Mar 12 2007 Steve Dickson <steved@redhat.com> 1.0.12-3
- Incorporated Merge Review comments (bz 226198)

* Fri Mar  9 2007 Steve Dickson <steved@redhat.com> 1.0.12-2
- Added condstop to all the initscripts (bz 196934)
- Made no_subtree_check a default export option (bz 212218)

* Tue Mar  6 2007 Steve Dickson <steved@redhat.com> 1.0.12-1
- Upgraded to 1.0.12 
- Fixed typo in Summary.

* Thu Mar  1 2007 Karel Zak <kzak@redhat.com>  1.0.11-2
- Fixed mount.nfs -f (fake) option (bz 227988)

* Thu Feb 22 2007 Steve Dickson <steved@redhat.com> 1.0.11-1
- Upgraded to 1.0.11 

* Wed Feb 21 2007 Steve Dickson <steved@redhat.com> 1.0.10-7
- Added FS_Location support

* Mon Dec 18 2006 Karel Zak <kzak@redhat.com> 1.0.10-6
- add support for mount options that contain commas (bz 219645)

* Wed Dec 13 2006 Steve Dickson <steved@redhat.com> 1.0.10-5
- Stopped v4 umounts from ping rpc.mountd (bz 215553)

* Tue Nov 28 2006 Steve Dickson <steved@redhat.com> 1.0.10-4
- Doing a connect on UDP sockets causes the linux network
  stack to reject UDP patches from multi-home server with
  nic on the same subnet. (bz 212471)

* Wed Nov 15 2006 Steve Dickson <steved@redhat.com> 1.0.10-3
- Removed some old mounting versioning code that was
  stopping tcp mount from working (bz 212471)

* Tue Oct 31 2006 Steve Dickson <steved@redhat.com> 1.0.10-2
- Fixed -o remount (bz 210346)
- fix memory leak in rpc.idmapd (bz 212547)
- fix use after free bug in dirscancb (bz 212547)
- Made no_subtree_check a default export option (bz 212218)

* Wed Oct 25 2006 Steve Dickson <steved@redhat.com> 1.0.10-1
- Upgraded to 1.0.10 

* Mon Oct 16 2006 Steve Dickson <steved@redhat.com> 1.0.9-10
- Fixed typo in nfs man page (bz 210864).

* Fri Oct 13 2006 Steve Dickson <steved@redhat.com> 1.0.9-9
- Unable to mount NFS V3 share where sec=none is specified (bz 210644)

* Tue Sep 26 2006 Steve Dickson <steved@redhat.com> 1.0.9-8
- mount.nfs was not returning a non-zero exit value 
  on failed mounts (bz 206705)

* Wed Sep 20 2006 Karel Zak <kzak@redhat.com> 1.0.9-7
- Added support for the mount -s (sloppy) option (#205038)
- Added nfs.5 man page from util-linux
- Added info about [u]mount.nfs to the package description

* Mon Sep 11 2006  <SteveD@RedHat.com> 1.0.9-6
- Removed the compiling of getiversion and getkversion since
  UTS_RELEASE is no longer defined and these binary are
  not installed.

* Fri Aug 18 2006 <SteveD@RedHat.com> 1.0.9-5
- Changed gssd daemons to cache things in memory
  instead of /tmp which makes selinux much happier.
  (bz 203078)

* Wed Aug 16 2006 <SteveD@RedHat.com> 1.0.9-4
- Allow variable for HA callout program in /etc/init.d/nfslock
  (bz 202790)

* Wed Aug 02 2006 <wtogami@redhatcom> 1.0.9-3
- add epoch (#196359)

* Fri Jul 28 2006 <SteveD@RedHat.com> 1.0.9-2
- Enabled the creating of mount.nfs and umount.nfs binaries
- Added mount option fixes suggested by upstream.
- Fix lazy umounts (bz 169299)
- Added -o fsc mount option.

* Mon Jul 24 2006 <SteveD@RedHat.com> 1.0.9-1
- Updated to 1.0.9 release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0.8-5.1
- rebuild

* Sun Jul  2 2006 <jkeating@redhat.com> 1:1.0.8-5
- Introduce epoch to fix upgrade path

* Sat Jul  1 2006 <SteveD@RedHat.com> 1.0.8-3
- Fixed typos in /etc/rc.d/init.d/nfs file (bz 184486)

* Fri Jun 30 2006 <SteveD@RedHat.com> 1.0.8-3
- Split the controlling of nfs version, ports, and protocol 
  into two different patches
- Fixed and added debugging statements to rpc.mountd.
- Fixed -p arg to work with priviledged ports (bz 156655)
- Changed nfslock initscript to set LOCKD_TCPPORT and
  LOCKD_UDPPORT (bz 162133)
- Added MOUNTD_NFS_V1 variable to version 1 of the
  mount protocol can be turned off. (bz 175729)
- Fixed gssd to handel mixed case characters in
  the domainname. (bz 186069)

* Wed Jun 21 2006 <SteveD@RedHat.com> 1.0.8-2
- Updated to nfs-utils-1.0.8

* Thu Jun  8 2006 <SteveD@RedHat.com> 1.0.8.rc4-1
- Upgraded to the upstream 1.0.8.rc4 version

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.8.rc2-4.FC5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.8.rc2-4.FC5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 20 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-4.FC5
- Added new libnfsidmap call, nfs4_set_debug(), to rpc.idmapd
  which turns on debugging in the libarary.

* Mon Jan 16 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-3.FC5
- Added innetgr patch that changes configure scripts to 
  check for the innetgr function. (bz 177899)

* Wed Jan 11 2006 Peter Jones <pjones@redhat.com> 1.0.8.rc2-2.FC5
- Fix lockfile naming in the initscripts so they're stopped correctly.

* Mon Jan  9 2006 Steve Dickson <SteveD@RedHat.com> 1.0.8.rc2-1.FC5
- Updated to 1.0.8-rc2 release
- Broke out libgssapi into its own rpm
- Move librpcsecgss and libnfsidmap in the new nfs-utils-lib rpm
- Removed libevent code; Required to be installed.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Oct 23 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-19
- Updated to latest code in SourceForge CVS
- Updated to latest CITI patches (1.0.7-4)
- Fix bug in nfsdreopen by compiling in server defaults

* Thu Sep 22 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-18
- Updated libnfsidmap to 0.11
- Updated libgssapi to 0.5
- Made sure the gss daemons and new libs are
  all using the same include files.
- Removed code from the tree that is no longer used.
- Add ctlbits patch that introduced the -N -T and -U
  command line flags to rpc.nfsd.

* Sun Sep 18 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-17
- Updated to latest nfs-utils code in upstream CVS tree
- Updated libevent from 1.0b to 1.1a
- Added libgssapi-0.4 and librpcsecgss-0.6 libs from CITI

* Thu Sep  8 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-16
- Reworked the nfslock init script so if lockd is running
  it will be killed which is what the HA community needs. (bz 162446)
- Stopped rpcidmapd.init from doing extra echoing when
  condstart-ed.

* Wed Aug 24 2005 Peter Jones <pjones@redhat.com> - 1.0.7-15
- don't strip during "make install", so debuginfo packages are generated right

* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- no need to still keep a requirement for kernel-2.2 or newer

* Tue Aug 16 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-13
- Changed mountd to use stat64() (bz 165062)

* Tue Aug  2 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-12
- Changed useradd to use new -l flag (bz149407)
- 64bit fix in gssd code (bz 163139)
- updated broken dependencies
- updated rquotad to compile with latest
  quota version.

* Thu May 26 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-8
- Fixed subscripting problem in idmapd (bz 158188)

* Thu May 19 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-7
- Fixed buffer overflow in rpc.svcgssd (bz 114288)

* Wed Apr 13 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-6
- Fixed misformated output from nfslock script (bz 154648)

* Tue Mar 29 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-4
- Fixed a compile error on x86_64 machines in the gss code.
- Updated the statd-notify-hostname.patch to eliminate 
  a segmentation fault in rpc.statd when an network 
  interface was down. (bz 151828)

* Sat Mar 19 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-3
- Changed xlog to use LOG_INFO instead of LOG_DEBUG
  so debug messages will appear w/out any config
  changes to syslog.conf.
- Reworked how /etc/exports is setup (bz 151389)

* Wed Mar  2 2005 Steve Dickson <SteveD@RedHat.com> 1.0.7-2
- Tied the rpcsecgss debugging in with gssd and
  svcgssd debugging

* Mon Feb 14 2005 Steve Dickson <SteveD@RedHat.com>
- Added support to rpcgssd.init and rpcsvcgssd.init scripts
  to insmod security modules.
- Changed the nfs.init script to bring rpc.svcgssd up and down,
  since rpc.svcgssd is only needed with the NFS server is running.

* Tue Dec 14 2004 Steve Dickson <SteveD@RedHat.com>
- Fix problem in idmapd that was causing "xdr error 10008"
  errors (bz 142813)
- make sure the correct hostname is used in the SM_NOTIFY
  message that is sent from a rebooted server which has 
  multiple network interfaces. (bz 139101)

- Changed nfslock to send lockd a -KILL signal
  when coming down. (bz 125257)

* Thu Nov 11 2004 Steve Dickson <SteveD@RedHat.com>
- Replaced a memcopy with explicit assignments
  in getquotainfo() of rquotad to fix potential overflow
  that can occur on 64bit machines. (bz 138068)

* Mon Nov  8 2004 Steve Dickson <SteveD@RedHat.com>
- Updated to latest sourceforge code
- Updated to latest CITIT nfs4 patches

* Sun Oct 17 2004 Steve Dickson <SteveD@RedHat.com>
- Changed nfs.init to bring down rquotad correctly
  (bz# 136041)

* Thu Oct 14 2004 Steve Dickson <SteveD@RedHat.com>
- Added "$RQUOTAD_PORT" variable to nfs.init which
  allows the rpc.rquotad to use a predefined port
  (bz# 124676)

* Fri Oct  1 2004 <SteveD@RedHat.com
- Incorporate some clean up code from Ulrich Drepper (bz# 134025)
- Fixed the chkconfig number in the rpcgssd, rpcidmapd, and 
  rpcsvcgssd initscrpts (bz# 132284)

* Fri Sep 24 2004 <SteveD@RedHat.com>
- Make sure the uid/gid of nfsnobody is the
  correct value for all archs (bz# 123900)
- Fixed some security issues found by SGI (bz# 133556)

* Mon Aug 30 2004 Steve Dickson <SteveD@RedHat.com>
- Major clean up. 
- Removed all unused/old patches
- Rename and condensed a number of patches
- Updated to CITI's nfs-utils-1.0.6-13 patches

* Tue Aug 10 2004 Bill Nottingham <notting@redhat.com>
- move if..fi condrestart stanza to %%postun (#127914, #128601)

* Wed Jun 16 2004 <SteveD@RedHat.com>
- nfslock stop is now done on package removals
- Eliminate 3 syslog messages that are logged for
  successful events.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jun 14 2004 <SteveD@RedHat.com>
- Fixed syntax error in nfs initscripts when
  NETWORKING is not defined
- Removed sync warning on readonly exports.
- Changed run levels in rpc initscripts.
- Replaced modinfo with lsmod when checking
  for loaded modules.

* Tue Jun  1 2004 <SteveD@RedHat.com>
- Changed the rpcgssd init script to ensure the 
  rpcsec_gss_krb5 module is loaded

* Tue May 18 2004 <SteveD@RedHat.com>
- Removed the auto option from MOUNTD_NFS_V2 and
  MOUNTD_NFS_V3 variables. Since v2 and v3 are on
  by default, there only needs to be away of 
  turning them off.

* Mon May 10 2004 <SteveD@RedHat.com>
- Rebuilt

* Thu Apr 15 2004 <SteveD@RedHat.com>
- Changed the permission on idmapd.conf to 644
- Added mydaemon code to svcgssd
- Updated the add_gssd.patch from upstream

* Wed Apr 14 2004 <SteveD@RedHat.com>
- Created a pipe between the parent and child so 
  the parent process can report the correct exit
  status to the init scripts
- Added SIGHUP processing to rpc.idmapd and the 
  rpcidmapd init script.

* Mon Mar 22 2004 <SteveD@RedHat.com>
- Make sure check_new_cache() is looking in the right place 

* Wed Mar 17 2004 <SteveD@RedHat.com>
- Changed the v4 initscripts to use $prog for the
  arugment to daemon

* Tue Mar 16 2004 <SteveD@RedHat.com>
- Made the nfs4 daemons initscripts work better when 
  sunrpc is not a module
- added more checks to see if modules are being used.

* Mon Mar 15 2004 <SteveD@RedHat.com>
- Add patch that sets up gssapi_mech.conf correctly

* Fri Mar 12 2004 <SteveD@RedHat.com>
- Added the shutting down of the rpc v4 daemons.
- Updated the Red Hat only patch with some init script changes.

* Thu Mar 11 2004 Bill Nottingham <notting@redhat.com>
- rpc_pipefs mounting and aliases are now in modutils; require that

* Thu Mar 11 2004 <SteveD@RedHat.com>
- Updated the gssd patch.

* Sun Mar  7 2004 <SteveD@RedHat.com>
- Added the addition and deletion of rpc_pipefs to /etc/fstab
- Added the addition and deletion of module aliases to /etc/modules.conf

* Mon Mar  1 2004 <SteveD@RedHat.com>
- Removed gssd tarball and old nfsv4 patch.
- Added new nfsv4 patches that include both the
   gssd and idmapd daemons
- Added redhat-only v4 patch that reduces the
   static librpc.a to only contain gss rpc related
   routines (I would rather have gssd use the glibc 
   rpc routines)
-Changed the gssd svcgssd init scripts to only
   start up if SECURE_NFS is set to 'yes' in
   /etc/sysconfig/nfs

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Thomas Woerner <twoerner@redhat.com>
- make rpc.lockd, rpc.statd, rpc.mountd and rpc.nfsd pie

* Wed Jan 28 2004 Steve Dickson <SteveD@RedHat.com>
- Added the NFSv4 bits

* Mon Dec 29 2003 Steve Dickson <SteveD@RedHat.com>
- Added the -z flag to nfsstat

* Wed Dec 24 2003  Steve Dickson <SteveD@RedHat.com>
- Fixed lockd port setting in nfs.int script

* Wed Oct 22 2003 Steve Dickson <SteveD@RedHat.com>
- Upgrated to 1.0.6
- Commented out the acl path for fedora

* Wed Aug  27 2003 Steve Dickson <SteveD@RedHat.com>
- Added the setting of lockd ports via sysclt interface
- Removed queue setting code since its no longer needed

* Thu Aug  7 2003 Steve Dickson <SteveD@RedHat.com>
- Added back the acl patch Taroon b2

* Wed Jul 23 2003 Steve Dickson <SteveD@RedHat.com>
- Commented out the acl patch (for now)

* Mon Jul 21 2003 Steve Dickson <SteveD@RedHat.com>
- Upgrated to 1.0.5

* Wed Jun 18 2003 Steve Dickson <SteveD@RedHat.com>
- Added security update
- Fixed the drop-privs.patch which means the chroot
patch could be removed.

* Mon Jun  9 2003 Steve Dickson <SteveD@RedHat.com>
- Defined the differ kinds of debugging avaliable for mountd in
the mountd man page. 

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Steve Dickson <SteveD@RedHat.com>
- Upgraded to 1.0.3 
- Fixed numerous bugs in init scrips
- Added nfsstat overflow patch

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 1.0.1-2.9
- rebuild

* Fri Dec 13 2002 Daniel J Walsh <dwalsh@redhat.com>
- change init script to not start rpc.lock if already running

* Wed Dec 11 2002 Daniel J Walsh <dwalsh@redhat.com>
- Moved access code to be after dropping privs

* Mon Nov 18 2002 Stephen C. Tweedie <sct@redhat.com>
- Build with %%configure
- Add nhfsgraph, nhfsnums and nhfsrun to the files list

* Mon Nov 11 2002 Stephen C. Tweedie <sct@redhat.com>
- Don't drop privs until we've bound the notification socket

* Thu Nov  7 2002 Stephen C. Tweedie <sct@redhat.com>
- Ignore SIGPIPE in rpc.mountd

* Thu Aug  1 2002 Bob Matthews <bmatthews@redhat.com>
- Add Sean O'Connell's <sean@ee.duke.edu> nfs control tweaks
- to nfs init script.

* Mon Jul 22 2002 Bob Matthews <bmatthews@redhat.com>
- Move to nfs-utils-1.0.1

* Mon Feb 18 2002 Bob Matthews <bmatthews@redhat.com>
- "service nfs restart" should start services even if currently 
-   not running (#59469)
- bump version to 0.3.3-4

* Wed Oct  3 2001 Bob Matthews <bmatthews@redhat.com>
- Move to nfs-utils-0.3.3
- Make nfsnobody a system account (#54221)

* Tue Aug 21 2001 Bob Matthews <bmatthews@redhat.com>
- if UID 65534 is unassigned, add user nfsnobody (#22685)

* Mon Aug 20 2001 Bob Matthews <bmatthews@redhat.com>
- fix typo in nfs init script which prevented MOUNTD_PORT from working (#52113)

* Tue Aug  7 2001 Bob Matthews <bmatthews@redhat.com>
- nfs init script shouldn't fail if /etc/exports doesn't exist (#46432)

* Fri Jul 13 2001 Bob Matthews <bmatthews@redhat.com>
- Make %%pre useradd consistent with other Red Hat packages.

* Tue Jul 03 2001 Michael K. Johnson <johnsonm@redhat.com>
- Added sh-utils dependency for uname -r in nfs init script

* Tue Jun 12 2001 Bob Matthews <bmatthews@redhat.com>
- make non RH kernel release strings scan correctly in 
-   nfslock init script (#44186)

* Mon Jun 11 2001 Bob Matthews <bmatthews@redhat.com>
- don't install any rquota pages in _mandir: (#39707, #44119)
- don't try to manipulate rpc.rquotad in init scripts 
-   unless said program actually exists: (#43340)

* Tue Apr 10 2001 Preston Brown <pbrown@redhat.com>
- don't translate initscripts for 6.x

* Tue Apr 10 2001 Michael K. Johnson <johnsonm@redhat.com>
- do not start lockd on kernel 2.2.18 or higher (done automatically)

* Fri Mar 30 2001 Preston Brown <pbrown@redhat.com>
- don't use rquotad from here now; quota package contains a version that 
  works with 2.4 (#33738)

* Mon Mar 12 2001 Bob Matthews <bmatthews@redhat.com>
- Statd logs at LOG_DAEMON rather than LOG_LOCAL5
- s/nfs/\$0/ where appropriate in init scripts

* Tue Mar  6 2001 Jeff Johnson <jbj@redhat.com>
- Move to nfs-utils-0.3.1

* Wed Feb 14 2001 Bob Matthews <bmatthews@redhat.com>
- #include <time.h> patch

* Mon Feb 12 2001 Bob Matthews <bmatthews@redhat.com>
- Really enable netgroups

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize initscripts

* Fri Jan 19 2001 Bob Matthews <bmatthews@redhat.com>
- Increased {s,r}blen in rpcmisc.c:makesock to accommodate eepro100

* Tue Jan 16 2001 Bob Matthews <bmatthews@redhat.com>
- Hackish fix in build section to enable netgroups

* Wed Jan  3 2001 Bob Matthews <bmatthews@redhat.com>
- Fix incorrect file specifications in statd manpage.
- Require gawk 'cause it's used in nfslock init script.

* Wed Dec 13 2000 Bob Matthews <bmatthews@redhat.com>
- Require sed because it's used in nfs init script

* Tue Dec 12 2000 Bob Matthews <bmatthews@redhat.com>
- Don't do a chroot(2) after dropping privs, in statd.

* Mon Dec 11 2000 Bob Matthews <bmatthews@redhat.com>
- NFSv3 if kernel >= 2.2.18, detected in init script

* Thu Nov 23 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.2.1

* Tue Nov 14 2000 Bill Nottingham <notting@redhat.com>
- don't start lockd on 2.4 kernels; it's unnecessary

* Tue Sep  5 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- more portable fix for mandir

* Sun Sep  3 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to 0.2-release

* Fri Sep  1 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- fix reload script

* Thu Aug 31 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to 0.2 from CVS
- adjust statd-drop-privs patch
- disable tcp_wrapper support

* Wed Aug  2 2000 Bill Nottingham <notting@redhat.com>
- fix stop priority of nfslock

* Tue Aug  1 2000 Bill Nottingham <notting@redhat.com>
- um, actually *include and apply* the statd-drop-privs patch

* Mon Jul 24 2000 Bill Nottingham <notting@redhat.com>
- fix init script ordering (#14502)

* Sat Jul 22 2000 Bill Nottingham <notting@redhat.com>
- run statd chrooted and as non-root
- add prereqs

* Tue Jul 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use "License", not "Copyright"
- use %%{_tmppath} and %%{_mandir}

* Mon Jul 17 2000 Matt Wilson <msw@redhat.com>
- built for next release

* Mon Jul 17 2000 Matt Wilson <msw@redhat.com>
- 0.1.9.1
- remove patch0, has been integrated upstream

* Wed Feb  9 2000 Bill Nottingham <notting@redhat.com>
- the wonderful thing about triggers, is triggers are wonderful things...

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- switch to nfs-utils as the base tree
- fix the statfs patch for the new code base
- single package that obsoletes everything we had before (if I am to keep
  some traces of my sanity with me...)

* Mon Jan 17 2000 Preston Brown <pbrown@redhat.com>
- use statfs syscall instead of stat to determinal optimal blksize
