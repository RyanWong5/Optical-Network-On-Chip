function simresult=simresext(fname)
% The function is to extract simulation result from the text file and
% convert to a matrix.
fid=fopen(fname);
fclose(fid);
fid=fopen(fname);
tline = fgetl(fid);
tline = fgetl(fid);
tline = fgetl(fid);
tline = fgetl(fid);
tline = fgetl(fid);
rindex = 1;
while ~feof(fid)
    tline = fgetl(fid);
    tline = replace(tline,'Right','1');
    tline = replace(tline,'Left ','2');
    tline = [str2num(tline(1,1:4)) str2num(tline(1,5:8)) str2num(tline(1,9:19)) str2num(tline(1,20:30)) str2num(tline(1,31:41)) str2num(tline(1,42:52)) str2num(tline(1,53:63)) str2num(tline(1,64:74)) str2num(tline(1,75:77)) str2num(tline(1,78))];
    simresult(rindex,:) = tline;
    rindex=rindex+1;
end
fclose(fid);