%global pubDir /var/www

Name:  		   helloworld
Version:       1.0.0
Release:	   0
Summary: 	   a rpm.
License:	   Commercial
%Description
This is a rpm.

%install
%__mkdir_p ${RPM_BUILD_ROOT}%{pubDir}
echo "hello world" > ${RPM_BUILD_ROOT}%{pubDir}/helloworld

%files
%{pubDir}/helloworld