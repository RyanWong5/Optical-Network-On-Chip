function visualsim
% The functions is to visualize the simulation result of different
% configurations to compare latency and cost.
for i=1:600
cost(1,i)=all(i).cost;
latency(1,i)=all(i).latency;
end

v(:,1) = cost;
v(:,2) = latency;
data = sortrows(v)';

x = 1:600;
y1 = data(1,:);
y2 = data(2,:);
[AX,H1,H2] = plotyy(x,y1,x,y2,'plot');
set(get(AX(2),'Ylabel'),'String','Average Transmission Cost'); 
set(get(AX(1),'Ylabel'),'String','Average Transmission Latency (Clock Cycle)') ;
xlabel('Configuration') ;
title('Transmission Cost V.S. Transmission Latency') ;