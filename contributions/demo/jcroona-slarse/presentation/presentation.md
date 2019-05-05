## Git under the hood

```bash
$ git init
$ echo "important" > file.txt
$ git add file.txt
$ git commit -m "Add file"
```

![Visualization of the .git/objects directory](gitviz.pdf){width=85%}

\begin{multicols}{2}

\begin{minipage}{.45\textwidth}
$$\textrm{git add} \approx 
\begin{cases}
    \textrm{git hash-object} \\
    \textrm{git update-index}
\end{cases}
$$
\end{minipage}

\begin{minipage}{.45\textwidth}
$$
\textrm{git commit} \approx
\begin{cases}
    \textrm{git write-tree} \\
    \textrm{git commit-tree}
\end{cases}
$$
\end{minipage}


\end{multicols}
