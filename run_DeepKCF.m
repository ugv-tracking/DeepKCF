function results = run_DeepKCF(seq, res_path, bSaveImage)

  pydata = py.dict(pyargs('path',seq.path,'nz',seq.nz, 'ext', seq.ext, ...
			  'startFrame',seq.startFrame, 'endFrame', seq.endFrame, ...
			  'len',seq.len, 'annoBegin',seq.annoBegin,...
			  'init_rect', seq.init_rect, 'name', seq.name));

%   pydata = py.dict(pyargs('path','Benchmark/Matrix/img/','nz',4, 'ext', 'jpg', ...
% 			      'startFrame',1, 'endFrame', 100, ...
% 			      'len', 100, 'annoBegin',1,...
% 			      'init_rect', [255 135 61 71], 'name', 'shaking_1'));
%   res_path='tmp';
%   bSaveImage=0;


  py_out=py.deepkcf.DeepKCF_OTB.DeepKCF(pydata, res_path, bSaveImage);

  data = double(py.array.array('d',py.numpy.nditer(py_out{1})));
  data = reshape(data, [4, length(data)/4])';

  results.fps = py_out{2};
  results.type='rect';
  results.res =data;
end