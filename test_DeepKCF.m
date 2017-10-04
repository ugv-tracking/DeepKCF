py.list;
pydata = py.dict(pyargs('path','Benchmark/Matrix/img/','nz',4, 'ext', 'jpg', ...
     'startFrame',1, 'endFrame', 100, ...
     'len', 100, 'annoBegin',1,...
     'init_rect', [255 135 61 71], 'name', 'shaking_1'));
 
res_path='tmp';
bSaveImage=0;

py_out=py.test_deepkcy.DeepKCF(pydata, res_path, bSaveImage);
%py.test_python.test();