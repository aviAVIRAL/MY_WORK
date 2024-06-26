%------------------------
\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.0in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
{#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
\begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
  \textbf{#1} & #2 \\
  \textit{\small#3} & \textit{\small #4} \\
\end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
\item
\begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
  \textit{\small#1} & \textit{\small #2} \\
\end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
\item
\begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
  \small#1 & #2 \\
\end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING----------


\begin{center}
\textbf{\Huge \scshape Aviral Sharma} \\ \vspace{1pt}
\small INDIA,Delhi-NCR $|$ 
\small +91 987-167-6949 $|$
\href{https://mail.google.com/mail/u/0/?pli=1#inbox}{\underline{aviralsharmaknp@gmail.com}} $|$ 
\href{https://www.linkedin.com/feed/}{\underline{linkedin/avi}} $|$
\href{https://github.com/aviAVIRAL/MY_WORK}{\underline{github/avi}} $|$
\href{https://leetcode.com/aviralsharmaknp/}{\underline{leetcode/avi}} $|$
    
\end{center}


%-----------EDUCATION-----------

\section{Education}
  \resumeSubHeadingListStart
\resumeSubheading
  {Krishna Institute of Engineering and Technology }{July 2022 - June 2024}
  {M.Tech in Computer Science Engineering (Curr SGPA: 9.6)}{Ghaziabad, UP}
\resumeSubheading
  {Krishna Engineering College}{Aug 2018 - May 2022}
  {B.Tech in Computer Science Engineering (GPA: 7.5)}{Ghaziabad, UP}
  
% \resumeSubheading
%   {Krishna Institute of Engineering and Technology }{July 2022 - May 2024}
%   {M.Tech in Computer Science Engineering (GPA: 7.53)}{Ghaziabad, UP}
% \resumeSubheading
%   {Krishna Engineering College}{Aug 2018 - May 2022}
%   {B.Tech in Computer Science Engineering (GPA: 7.5)}{Ghaziabad, UP}
  
  
  \resumeSubHeadingListEnd


% %-----------EXPERIENCE-----------
% \section{Experience}
%   \resumeSubHeadingListStart

%     \resumeSubheading
%       {InnoBit Systems Pvt Ltd}{Dec 2021 - Feb 2022}
%       {DevOps Engineer}{Noida, UP}
%       \resumeItemListStart
%         \resumeItem{Developed secure login pages with functionality, incorporating best practices for user authentication and authorization. ensuring a seamless and user-friendly interface}
%         \resumeItem{Created responsive web pages using React, ensuring optimal user experiences across devices}
        
%       \resumeItemListEnd
      


%   \resumeSubHeadingListEnd


%-----------PROJECTS-----------
\section{Projects}
\resumeSubHeadingListStart
    
% ......................................................
   \resumeProjectHeading
      {\textbf{Interactive Story Generation Developer}  \emph{       }}{Oct 2023 -- Present}
      \resumeItemListStart
        \resumeItem{Developed JARVAS (Just Another Responsive Virtual Assistant), a system for interactive story generation.}
        \resumeItem{Integrated Google Speech-to-Text technology for prompt input.}
        \resumeItem{Integrated Google Gemini Pro model for story generation.}
        \resumeItem{Implemented text-to-speech conversion for audio playback and database storage for story archiving.}
          
% .......................key features .........
        \resumeItem{\textbf{Key Features:}}
        \resumeItem{Wake-up command activation $|$ Speech-to-Text and Text-to-Speech conversion}
        \resumeItem{Prompt processing and story generation $|$ Database storage for story retrieval}
% .................benifits.......................
        \resumeItem{\textbf{Benefits:}}
        \resumeItem{Interactive storytelling experience $|$ Seamless integration with Google services}
        \resumeItem{Personalized storytelling based on user inputs $|$ Enhanced accessibility through audio playback }

% ...............................................
         \textbf{\href{https://drive.google.com/drive/u/2/home}{\textbf{video.link/avi}}} {$|$} {\href{https://github.com/aviAVIRAL/MY_WORK/tree/main/1.%20PROJECTS}{\textbf{github.com/avi}}}\\
            
      \resumeItemListEnd

% ......................................................
    
  \resumeProjectHeading
      {\textbf{Phone Number Tracker} $|$ \emph{Python, phonenumbers, Folium, geocoder, OpenCageGeocodeAPI}}{June 2023 -- July 2023}
      \resumeItemListStart
        \resumeItem{Developed a cutting-edge Phone Number Tracker system using Python, providing users with a seamless experience to track phone number locations.}
        \resumeItem{Utilized the robust phonenumbers library for accurate phone number validation, ensuring reliable results.}
        \resumeItem{Integrated geocoding technology with the geocoder library and OpenCageGeocode API, delivering precise location details for enhanced user satisfaction.}
        \resumeItem{Implemented dynamic map visualization using Folium, enabling users to intuitively visualize phone number locations.}
        \resumeItem{Implemented Folium for interactive map visualization.}
        \resumeItem{Demonstrates proficiency in Python libraries and APIs to create a practical and user-friendly solution for location tracking.}

 \textbf{\href{https://drive.google.com/drive/u/1/home}{\textbf{video.link/avi}}} {$|$} {\href{https://github.com/aviAVIRAL/MY_WORK/tree/main/1.%20PROJECTS/Project%201%20TRACK%20PHONE%20NUMBER}{\textbf{github.com/avi}}}\\
            
      \resumeItemListEnd
          
  % \resumeProjectHeading
  %     {\textbf{Movie recommendation system} $|$ \emph{Python, Deep Learning, Pandas, scikit-learn}}{May 2023 -- May 2023}
  %     \resumeItemListStart
  %       \resumeItem{Developed a personalized movie recommendation system using Python.}
  %       \resumeItem{employing deep learning and machine learning algorithms.}
  %       \resumeItem{Collaborated with the MovieLens dataset, utilizing pandas and scikit-learn for comprehensive data analysis with the MovieLens dataset.}
  %       \resumeItem{Analyzed user preferences and historical data to suggest personalized movie recommendations}

  %        \textbf{\href{https://drive.google.com/drive/u/1/home}{\textbf{video.link/avi}}} {$|$} {\href{https://github.com/aviAVIRAL/MY_WORK/tree/main/1.%20PROJECTS/Project%201%20TRACK%20PHONE%20NUMBER}{\textbf{github.com/avi}}}\\
            
  %     \resumeItemListEnd




          
\resumeSubHeadingListEnd



%
%-----------Technical Skills-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
\small{\item{
 \textbf{Languages}{: Python, C, C++} \\
 \textbf{Web development}{: JavaScript, HTML, CSS} \\
 \textbf{Development Environment}{: Visual Studio Code, PyCharm, Git} \\
     
 \textbf{Libraries}{: Folium, geocoder, pandas, NumPy, scikit-learn, TensorFlow, PyTorch etc.} \\
 \textbf{Coursework}{: DSA, OOPs, DBMS.  } \\
% full subject like hai icomment
 % \textbf{Coursework}{: DSA, OOPs, OS, Cloud, ANSI SQL, CN, DBMS  } \\
     
    
}}
 \end{itemize}

% ....................................................



%///////aageivementS-----------
\section{Achievements}
 \begin{itemize}[leftmargin=0.15in, label={}]
\small{\item{
     
 \textbf{Football}{: Play regional level football as left winger} \\
     
 \textbf{Chess Rating}{: Global rating Blitz 776 $|$ 3814+ games play $|$} {\href{https://www.chess.com/stats/overview/aviralsharmaknp/0?}{\textbf{chess.com/avi}}}\\
     
 \textbf{TCS CodeVita}{: TCS CodeVita S-10 global rank 5.4k $|$ India rank under 2k $|$} {\href{https://drive.google.com/file/d/11AlrrltA985cYADN4LY8U_vni2o0B9Ll/view?usp=drive_link}{\textbf{drive.com/avi}}}\\
     
     
 \textbf{DSA}{: 400+ Questions solved in different platforms (CC, CF, AC, LC) $|$} {\href{https://leetcode.com/aviralsharmaknp/}{\textbf{leetcode.com/avi}}}\\
     
     
     
     
  
    

     
}}
 \end{itemize}






%-------------------------------------------
\end{document}




