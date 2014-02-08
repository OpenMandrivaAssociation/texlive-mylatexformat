# revision 21392
# category Package
# catalog-ctan /macros/latex/contrib/mylatexformat
# catalog-date 2011-02-13 01:21:30 +0100
# catalog-license lppl1.3
# catalog-version 3.4
Name:		texlive-mylatexformat
Version:	3.4
Release:	3
Summary:	Build a format based on the preamble of a LaTeX file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mylatexformat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The use of formats helps to speed up compilations: packages
which have been dumped in the format are loaded at very high
speed. This is useful when a document loads many packages
(including large packages such as pgf-TikZ). The package was
developed from the work in mylatex, and eliminates many of the
limitations and problems of that package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mylatexformat/mylatexformat.ltx
%doc %{_texmfdistdir}/doc/latex/mylatexformat/README
%doc %{_texmfdistdir}/doc/latex/mylatexformat/mylatexformat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mylatexformat/mylatexformat.drv
%doc %{_texmfdistdir}/source/latex/mylatexformat/mylatexformat.dtx
%doc %{_texmfdistdir}/source/latex/mylatexformat/mylatexformat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.4-2
+ Revision: 754244
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.4-1
+ Revision: 719097
- texlive-mylatexformat
- texlive-mylatexformat
- texlive-mylatexformat
- texlive-mylatexformat

