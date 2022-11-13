Name:		texlive-mylatexformat
Version:	21392
Release:	1
Summary:	Build a format based on the preamble of a LaTeX file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mylatexformat
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mylatexformat.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
