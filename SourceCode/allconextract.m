function allconextract
%This function is to extract all configurations from all result text files
%in the folder.
allfiles=dir;
filenum=size(allfiles,1)-2;
%allcon=char(zeros(filenum,37));
allcon=zeros(filenum,16);
for i=3:filenum+2
    filename=allfiles(i).name;
    filenamenum=str2num(filename(1,1:3));
    adjust=size(num2str(filenamenum),2)-1;
    raw=textread(filename,'%c');
    config=raw(84+adjust:120+adjust,1)';
    config=replace(config,',',' ');
    %config=string(config)
    config=str2num(config);
    allcon(i-2,:)=config;
end
dlmwrite('allcon.txt',allcon);
    