function all=allanlz
allfiles=dir;
filenum=size(allfiles,1)-2;
for i=1:filenum
    fname=allfiles(i+2).name;
    simresult=simresext(fname);
    all(i).data=simresult;
    all(i).cost=mean(simresult(:,8));
    all(i).latency=mean(simresult(:,5)-simresult(:,4)-2);
end
