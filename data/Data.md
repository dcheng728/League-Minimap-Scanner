
<h1 id="league-map-scanner-v-1.0.0">League Map Scanner (V 1.0.0)</h1>
<p><strong>Data V1.0.0</strong><br>
As of Version 7/4/2019, the program supports 31 champions:   (order corresponds to output position from CNN)</p>
<p>[‘ashe’, ‘blitzcrank’, ‘brand’, ‘caitlyn’, ‘cassiopeia’, ‘darius’, ‘drmundo’, ‘ezreal’, ‘fiddlestick’,’ garen’, ‘graves’, ‘jax’, ‘karthus’, ‘kayle’, ‘malphite’, ‘nasus’, ‘nidalee’, ‘renekton’, ‘ryze’, ‘shen’,’ sivir’, ‘soraka’, ‘tristana’, ‘trundle’, ‘udyr’, ‘vladimir’, ‘warwick’, ‘wukong’, ‘ziggs’, ‘zilean’, ‘zyra’]</p>
<p><a href="https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing)">https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing)</a>.<br>
I will keep updating the algorithm to support more champions and increase the accuracy :)</p>
<p><img src="demo.gif" alt=""></p>
<p><strong>Required dependencies:</strong><br>
Opencv, Tensorflow, Numpy, PIL</p>
<h3 id="preparing-environment-using-anaconda-same-method-for-windows-and-osx">Preparing environment using Anaconda, same method for Windows and OSX:</h3>
<ol>
<li>
<p>Start Anaconda Navigator, select environments on the left-hand bar, and click the triangle next to the environment you wish to run this program on and click “open Terminal”</p>
</li>
<li>
<p>Type in the following code in terminal:</p>
<pre><code> conda install -c conda-forge opencv
 conda install -c conda-forge numpy
 conda install -c conda-forge tensorflow
 conda install -c conda-forge pillow
</code></pre>
</li>
<li>
<p>Clone <a href="https://github.com/dcheng728/League-Minimap-Scanner/tree/master/League%20Minimap%20Scanner%20v%201.0.0" title="League Minimap Scanner v 1.0.0">League Minimap Scanner v 1.0.0</a> from this repository, and run <a href="http://liveidentify.py">liveidentify.py</a> once you finished downloading.</p>
</li>
</ol>
<h2 id="overview">Overview</h2>
<p>This Application aims to recognize League of Legends champions by examining the Minimap. The Algorithm takes an image of the minimap as input and returns the coordinates of enemy champions.</p>
<p>The Algorithm is composed of 2 parts:</p>
<p>1: Image Processing ( <a href="http://process.py">process.py</a> , <a href="http://live.py">live.py</a> )</p>
<p>2: Neural Network Evaluation ( <a href="http://image2numpy.py">image2numpy.py</a> , <a href="http://cnn.py">cnn.py</a> , <a href="http://evaluate.py">evaluate.py</a> )</p>
<p><em><strong>A Diagram of the Algorithm</strong></em></p>
<div class="mermaid"><svg xmlns="http://www.w3.org/2000/svg" id="mermaid-svg-w7sMhyqjoHXwc3vV" width="100%" viewBox="0 0 841.34375 446"><g transform="translate(-12, -12)"><g class="output"><g class="clusters"></g><g class="edgePaths"><g class="edgePath"><path class="path" d="M101.4375,235L126.4375,235L151.4375,235" marker-end="url(#arrowhead8567)"></path><defs><marker id="arrowhead8567" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M315.87681442541657,147.86692299783937L387.046875,43L412.71875,43" marker-end="url(#arrowhead8568)"></path><defs><marker id="arrowhead8568" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M341.5226845464504,172.53925608808785L387.046875,139L412.9609375,139" marker-end="url(#arrowhead8569)"></path><defs><marker id="arrowhead8569" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M362.046875,235L387.046875,235L412.7890625,235" marker-end="url(#arrowhead8570)"></path><defs><marker id="arrowhead8570" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M341.5226845464504,297.4607439119121L387.046875,331L412.046875,331" marker-end="url(#arrowhead8571)"></path><defs><marker id="arrowhead8571" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M315.87681442541657,322.13307700216063L387.046875,427L413.515625,427" marker-end="url(#arrowhead8572)"></path><defs><marker id="arrowhead8572" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M519.1875,43L544.859375,43L622.2166304790561,183.64274452094392" marker-end="url(#arrowhead8573)"></path><defs><marker id="arrowhead8573" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M518.9453125,139L544.859375,139L608.6535611367694,197.20581386323062" marker-end="url(#arrowhead8574)"></path><defs><marker id="arrowhead8574" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M519.1171875,235L544.859375,235L570.359375,235.5" marker-end="url(#arrowhead8575)"></path><defs><marker id="arrowhead8575" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M519.859375,331L544.859375,331L608.6535611367694,273.7941861367694" marker-end="url(#arrowhead8576)"></path><defs><marker id="arrowhead8576" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M518.390625,427L544.859375,427L622.2166304790561,287.35725547905605" marker-end="url(#arrowhead8577)"></path><defs><marker id="arrowhead8577" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M679.0958695209439,183.64274452094392L755.453125,43L783.3125,43" marker-end="url(#arrowhead8578)"></path><defs><marker id="arrowhead8578" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M692.6589388632306,197.20581386323062L755.453125,139L786.8125,139" marker-end="url(#arrowhead8579)"></path><defs><marker id="arrowhead8579" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M730.953125,235.5L755.453125,235L786.1328125,235" marker-end="url(#arrowhead8580)"></path><defs><marker id="arrowhead8580" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M692.6589388632306,273.7941861367694L755.453125,331L782.71875,331" marker-end="url(#arrowhead8581)"></path><defs><marker id="arrowhead8581" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g><g class="edgePath"><path class="path" d="M679.0958695209439,287.35725547905605L755.453125,427L780.453125,427" marker-end="url(#arrowhead8582)"></path><defs><marker id="arrowhead8582" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"></g></g></g></g></g></svg><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="edgeLabel" transform=""><g transform="translate(0,0)" class="label"><div xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></g></g><g class="nodes"><g class="node" id="A" transform="translate(60.71875,235)"><rect rx="0" ry="0" x="-40.71875" y="-23" width="81.4375" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-30.71875,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Minimap<div xmlns="http://www.w3.org/1999/xhtml">Minimap</div></div></g></g></g><g class="node" id="B" transform="translate(256.7421875,235)"><circle x="-105.3046875" y="-23" r="105.3046875"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-95.3046875,-13)"></g></g></g></g></div><p><strong>Data V1.0.0</strong><br>
As of Version 7/4/2019, the program supports 31 champions:   (order corresponds to output position from CNN)</p>
<p>[‘
</p><p>[‘ashe’’, ‘‘blitzcrank’’, ‘‘brand’’, ‘‘caitlyn’’, ‘‘cassiopeia’’, ‘‘darius’’, ‘‘drmundo’’, ‘‘ezreal’’, ‘‘fiddlestick’,’’,’ garen’’, ‘‘graves’’, ‘‘jax’’, ‘‘karthus’’, ‘‘kayle’’, ‘‘malphite’’, ‘‘nasus’’, ‘‘nidalee’’, ‘‘renekton’’, ‘‘ryze’’, ‘‘shen’,’’,’ sivir’’, ‘‘soraka’’, ‘‘tristana’’, ‘‘trundle’’, ‘‘udyr’’, ‘‘vladimir’’, ‘‘warwick’’, ‘‘wukong’’, ‘‘ziggs’’, ‘‘zilean’’, ‘'zyra’]</p>
<p></p><p>https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing)"&gt;https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing).<br>.<br>
I will keep updating the algorithm to support more champions and increase the accuracy :)</p>
<p><img src="demo.gif" alt=""></p>
<p><strong>
</strong></p><p><img src="demo.gif" alt=""></p>
<p><strong>Required dependencies:</strong><br><br>
Opencv, Tensorflow, Numpy, PIL</p>
<h3 id="preparing-environment-using-anaconda-same-method-for-windows-and-osx">
</h3><h3 id="preparing-environment-using-anaconda-same-method-for-windows-and-osxh3">Preparing environment using Anaconda, same method for Windows and OSX:</h3>
<ol>
<li>
<p>
</p></li></ol><ol>
<li>Start Anaconda Navigator, select environments on the left-hand bar, and click the triangle next to the environment you wish to run this program on and click “open Terminal”</li>
</ol>

<li>
<p>
2. Type in the following code in terminal:</p>
<pre><code>
</code><pre><code>    conda install -c conda-forge opencv
    conda install -c conda-forge numpy
    conda install -c conda-forge tensorflow
    conda install -c conda-forge pillow
</code></pre>
</pre></li><p></p>

<li>
<p>Clone <a href="3. Clone [League Minimap Scanner v 1.0.0](https://github.com/dcheng728/League-Minimap-Scanner/tree/master/League%20Minimap%20Scanner%20v%201.0.0" title="League Minimap Scanner v 1.0.0">League Minimap Scanner v 1.0.0</a> from this repository, and run <a href="http://liveidentify.py">liveidentify.py</a> once you finished downloading.</p>
</li>

<h2 id="overview">Overview</h2>
<p>) from this repository, and run liveidentify.py once you finished downloading.
</p><h2 id="overview">Overview</h2>
<p>This Application aims to recognize League of Legends champions by examining the Minimap. The Algorithm takes an image of the minimap as input and returns the coordinates of enemy champions.</p>
<p>
</p><p>The Algorithm is composed of 2 parts:</p>
<p>
</p><p>1: Image Processing ( <a href="http://process.py">process.py</a> , <a href="http://live.py">live.py</a> )</p>
<p>2: Neural Network Evaluation ( <a href="http://image2numpy.py">image2numpy.py</a> , <a href="http://cnn.py">cnn.py</a> , <a href="http://evaluate.py">evaluate.py</a> )</p>
<h2 id="image-processing">process.py , live.py )
</h2><p>2: Neural Network Evaluation ( <a href="http://image2numpy.py">image2numpy.py</a> , <a href="http://cnn.py">cnn.py</a> , <a href="http://evaluate.py">evaluate.py</a> )</p>
<h2 id="image-processingh2">Image Processing</h2>
<p>
</p><p>The Image Processing component is responsible for preprocessing the minimap images before feeding it into the neural network. To reduce the computational cost of the neural network, the preprocessing  component will cut out the minimap regions where a champion icon’'s ring is detected using Opencv, whose process is as follows:</p>
<ol>
<li>
<p>
</p></li></ol><ol>
<li>split 3-d image into b,g,r channels</li>
</ol>

<li>
<p>
</p></li><ol start="2">
<li>use inRange function to binarize the b,g,r channels</li>
</ol>

<li>
<p>
</p></li><ol start="3">
<li>deduct b and g from red channel to isolate the red channel (the color of enemy champions’’ rings)</li>
</ol>

<li>
<p>
</p></li><ol start="4">
<li>Run HoughCircles function to detect the red circles in red channel</li>
</ol>

<li>
<p>
</p></li><ol start="5">
<li>Cut out squares based on coordinates of the circles and output them</li>
</ol>


<p>
</p><p>After processing the image, the only inputs to the Neural Network are five 24*24 numpy arrays, which is much more computationally efficient compared to running object detection NN over the entire  minimap.</p>
<h2 id="neural-network">
</h2><h2 id="neural-networkh2">Neural Network</h2>
<p>
</p><p>The neural network is trained on 31 champions with roughly 360 images each. The size of training images numpy is (19000+,24,24,3) and such for test images is (1000+,24,24,3). To collect the data, an AutoHotKey  script was written. Once initiated, the script would start a training game from the League of Legends  Client, select friendly champion and enemy champion and start the game with a python program constantly  grabbing the [805:1080,1645:1920] pixels of the monitor. Then the script will process the images itself  and cut out the champions’’ portraits automatically.</p>
<p>
</p><p>The advantage to this approach is a small training dataset size and fast training. The over 20,000<br><br>
images only took up 35MB of space when saved as “".npy”" files. Training the NN for 10 epochs took less  than 30 seconds on a gaming laptop.</p>
<p>
</p><p>A weakness of the data collecting method is the deficiency of champions to choose from in League of Legends’’ practicetool. To collect training samples of all champions, the screen-grabbing program would have to overlook actual games, and the champion portraits might need to be labeled manually. In future versions, this algorithm will learn to recognize more champions, and I will be able to justify playing  League of Legends as ““researching”” :)</p>
<p>
</p><p>The training data are kept in /data/, train_images.npy (19000+,24,24,3), test_images.npy (1000+,24,24,3).</p>style="max-width: 841.34375px;" viewBox="0 0 841.34375 446"><g transform="translate(-12, -12)"><g class="output"><g class="clusters"></g><g class="edgePaths"><g class="edgePath" style="opacity: 1;"><path class="path" d="M101.4375,235L126.4375,235L151.4375,235" marker-end="url(#arrowhead8567)" style="fill:none"></path><defs><marker id="arrowhead8567" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M315.87681442541657,147.86692299783937L387.046875,43L412.71875,43" marker-end="url(#arrowhead8568)" style="fill:none"></path><defs><marker id="arrowhead8568" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M341.5226845464504,172.53925608808785L387.046875,139L412.9609375,139" marker-end="url(#arrowhead8569)" style="fill:none"></path><defs><marker id="arrowhead8569" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M362.046875,235L387.046875,235L412.7890625,235" marker-end="url(#arrowhead8570)" style="fill:none"></path><defs><marker id="arrowhead8570" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M341.5226845464504,297.4607439119121L387.046875,331L412.046875,331" marker-end="url(#arrowhead8571)" style="fill:none"></path><defs><marker id="arrowhead8571" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M315.87681442541657,322.13307700216063L387.046875,427L413.515625,427" marker-end="url(#arrowhead8572)" style="fill:none"></path><defs><marker id="arrowhead8572" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M519.1875,43L544.859375,43L622.2166304790561,183.64274452094392" marker-end="url(#arrowhead8573)" style="fill:none"></path><defs><marker id="arrowhead8573" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M518.9453125,139L544.859375,139L608.6535611367694,197.20581386323062" marker-end="url(#arrowhead8574)" style="fill:none"></path><defs><marker id="arrowhead8574" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M519.1171875,235L544.859375,235L570.359375,235.5" marker-end="url(#arrowhead8575)" style="fill:none"></path><defs><marker id="arrowhead8575" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M519.859375,331L544.859375,331L608.6535611367694,273.7941861367694" marker-end="url(#arrowhead8576)" style="fill:none"></path><defs><marker id="arrowhead8576" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M518.390625,427L544.859375,427L622.2166304790561,287.35725547905605" marker-end="url(#arrowhead8577)" style="fill:none"></path><defs><marker id="arrowhead8577" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M679.0958695209439,183.64274452094392L755.453125,43L783.3125,43" marker-end="url(#arrowhead8578)" style="fill:none"></path><defs><marker id="arrowhead8578" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M692.6589388632306,197.20581386323062L755.453125,139L786.8125,139" marker-end="url(#arrowhead8579)" style="fill:none"></path><defs><marker id="arrowhead8579" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M730.953125,235.5L755.453125,235L786.1328125,235" marker-end="url(#arrowhead8580)" style="fill:none"></path><defs><marker id="arrowhead8580" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M692.6589388632306,273.7941861367694L755.453125,331L782.71875,331" marker-end="url(#arrowhead8581)" style="fill:none"></path><defs><marker id="arrowhead8581" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g><g class="edgePath" style="opacity: 1;"><path class="path" d="M679.0958695209439,287.35725547905605L755.453125,427L780.453125,427" marker-end="url(#arrowhead8582)" style="fill:none"></path><defs><marker id="arrowhead8582" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="strokeWidth" markerWidth="8" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowheadPath" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker></defs></g></g><g class="edgeLabels"><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"></g></g></g></g></g></svgforeignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></gforeignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></gforeignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></gforeignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></gforeignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></gforeignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel" transform="" style="opacity: 1;"><g transform="translate(0,0)" class="label"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node" id="A" transform="translate(60.71875,235)" style="opacity: 1;"><rect rx="0" ry="0" x="-40.71875" y="-23" width="81.4375" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-30.71875,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Minimap</divforeignObject width="61.4375" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Minimap</div></foreignObject></g></g></g><g class="node" id="B" transform="translate(256.7421875,235)" style="opacity: 1;"><circle x="-105.3046875" y="-23" r="105.3046875"></circle><g class="label" transform="translate(0,0)"><g transform="translate(-95.3046875,-13)"><div xmlns="http://www.w3.org/1999/xhtmlforeignObject width="190.609375" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">OPENCV Image Processing</div></foreignObject></g></g></g><g class="node" id="D" transform="translate(465.953125,43)" style="opacity: 1;"><rect rx="0" ry="0" x="-53.234375" y="-23" width="106.46875" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-43.234375,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Champion A</divforeignObject width="86.46875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Champion A</div></foreignObject></g></g></g><g class="node" id="E" transform="translate(465.953125,139)" style="opacity: 1;"><rect rx="0" ry="0" x="-52.9921875" y="-23" width="105.984375" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-42.9921875,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Champion B</divforeignObject width="85.984375" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Champion B</div></foreignObject></g></g></g><g class="node" id="F" transform="translate(465.953125,235)" style="opacity: 1;"><rect rx="0" ry="0" x="-53.1640625" y="-23" width="106.328125" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-43.1640625,-13)"><div xmlns="http://www.w3.org/1999/xhtmlforeignObject width="86.328125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Champion C</div></foreignObject></g></g></g><g class="node" id="G" transform="translate(465.953125,331)" style="opacity: 1;"><rect rx="0" ry="0" x="-53.90625" y="-23" width="107.8125" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-43.90625,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Champion D</divforeignObject width="87.8125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Champion D</div></foreignObject></g></g></g><g class="node" id="H" transform="translate(465.953125,427)" style="opacity: 1;"><rect rx="0" ry="0" x="-52.4375" y="-23" width="104.875" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-42.4375,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Champion E</divforeignObject width="84.875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Champion E</div></foreignObject></g></g></g><g class="node" id="L" transform="translate(650.15625,235)" style="opacity: 1;"><polygon points="80.296875,0 160.59375,-80.296875 80.296875,-160.59375 0,-80.296875" rx="5" ry="5" transform="translate(-80.296875,80.296875)"></polygon><g class="label" transform="translate(0,0)"><g transform="translate(-56.21875,-13)"><div xmlns="http://www.w3.org/1999/xhtmlforeignObject width="112.4375" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Neural Network</div></foreignObject></g></g></g><g class="node" id="Q" transform="translate(812.8984375,43)" style="opacity: 1;"><rect rx="0" ry="0" x="-29.5859375" y="-23" width="59.171875" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-19.5859375,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Riven</divforeignObject width="39.171875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Riven</div></foreignObject></g></g></g><g class="node" id="R" transform="translate(812.8984375,139)" style="opacity: 1;"><rect rx="0" ry="0" x="-26.0859375" y="-23" width="52.171875" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-16.0859375,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Elise</divforeignObject width="32.171875" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Elise</div></foreignObject></g></g></g><g class="node" id="S" transform="translate(812.8984375,235)" style="opacity: 1;"><rect rx="0" ry="0" x="-26.765625" y="-23" width="53.53125" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-16.765625,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Ryze</divforeignObject width="33.53125" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Ryze</div></foreignObject></g></g></g><g class="node" id="T" transform="translate(812.8984375,331)" style="opacity: 1;"><rect rx="0" ry="0" x="-30.1796875" y="-23" width="60.359375" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-20.1796875,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Kai'sa</divforeignObject width="40.359375" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Kai'sa</div></foreignObject></g></g></g><g class="node" id="U" transform="translate(812.8984375,427)" style="opacity: 1;"><rect rx="0" ry="0" x="-32.4453125" y="-23" width="64.890625" height="46"></rect><g class="label" transform="translate(0,0)"><g transform="translate(-22.4453125,-13)"><div xmlns="http://www.w3.org/1999/xhtml">Alistar</div></g></g></g></foreignObject width="44.890625" height="26"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; white-space: nowrap;">Alistar</div></foreignObject></g></g></g></g></g></g></svg></div>
<h2 id="image-processing">Image Processing</h2>
<p>The Image Processing component is responsible for preprocessing the minimap images before feeding it into the neural network. To reduce the computational cost of the neural network, the preprocessing  component will cut out the minimap regions where a champion icon’s ring is detected using Opencv, whose process is as follows:</p>
<ol>
<li>
<p>split 3-d image into b,g,r channels</p>
</li>
<li>
<p>use inRange function to binarize the b,g,r channels</p>
</li>
<li>
<p>deduct b and g from red channel to isolate the red channel (the color of enemy champions’ rings)</p>
</li>
<li>
<p>Run HoughCircles function to detect the red circles in red channel</p>
</li>
<li>
<p>Cut out squares based on coordinates of the circles and output them</p>
</li>
</ol>
<p>After processing the image, the only inputs to the Neural Network are five 24*24 numpy arrays, which is much more computationally efficient compared to running object detection NN over the entire  minimap.</p>
<h2 id="neural-network">Neural Network</h2>
<p>The neural network is trained on 31 champions with roughly 360 images each. The size of training images numpy is (19000+,24,24,3) and such for test images is (1000+,24,24,3). To collect the data, an AutoHotKey  script was written. Once initiated, the script would start a training game from the League of Legends  Client, select friendly champion and enemy champion and start the game with a python program constantly  grabbing the [805:1080,1645:1920] pixels of the monitor. Then the script will process the images itself  and cut out the champions’ portraits automatically.</p>
<p>The advantage to this approach is a small training dataset size and fast training. The over 20,000<br>
images only took up 35MB of space when saved as “.npy” files. Training the NN for 10 epochs took less  than 30 seconds on a gaming laptop.</p>
<p>A weakness of the data collecting method is the deficiency of champions to choose from in League of Legends’ practicetool. To collect training samples of all champions, the screen-grabbing program would have to overlook actual games, and the champion portraits might need to be labeled manually. In future versions, this algorithm will learn to recognize more champions, and I will be able to justify playing  League of Legends as “researching” :)</p>
<p>The training data are kept in /data/, train_images.npy (19000+,24,24,3), test_images.npy (1000+,24,24,3).</p># League Map Scanner (V 1.0.0)
<p><strong>Data V1.0.0</strong><br>

**Data V1.0.0**
As of Version 7/4/2019, the program supports 31 champions:   (order corresponds to output position from CNN)</p>
<p>[‘

['ashe’', ‘'blitzcrank’', ‘'brand’', ‘'caitlyn’', ‘'cassiopeia’', ‘'darius’', ‘'drmundo’', ‘'ezreal’', ‘'fiddlestick’,’',' garen’', ‘'graves’', ‘'jax’', ‘'karthus’', ‘'kayle’', ‘'malphite’', ‘'nasus’', ‘'nidalee’', ‘'renekton’', ‘'ryze’', ‘'shen’,’',' sivir’', ‘'soraka’', ‘'tristana’', ‘'trundle’', ‘'udyr’', ‘'vladimir’', ‘'warwick’', ‘'wukong’', ‘'ziggs’', ‘'zilean’', ‘'zyra’]</p>
<p><a href="']

https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing)">https://drive.google.com/drive/folders/1Yg0pzLheTi2sPPF1HU7qiXxPSZyb3_th?usp=sharing(increasing)</a>.<br>.
I will keep updating the algorithm to support more champions and increase the accuracy :)</p>
<p><img src="demo.gif" alt=""></p>
<p><strong>



![](demo.gif)



**Required dependencies:</strong><br>**
Opencv, Tensorflow, Numpy, PIL</p>
<h3 id="preparing-environment-using-anaconda-same-method-for-windows-and-osx">```mermaid
graph LR
A[Minimap] --> B((OPENCV Image Processing))
B --> D[Champion A]
B --> E[Champion B]
B --> F[Champion C]
B --> G[Champion D]
B --> H[Champion E]
D--> L{Neural Network}
E --> L{Neural Network}
F --> L{Neural Network}
G --> L{Neural Network}
H --> L{Neural Network}
L --> Q[Riven]
L --> R[Elise]
L --> S[Ryze]
L --> T[Kai'sa]
L --> U[Alistar]
```

### Preparing environment using Anaconda, same method for Windows and OSX:</h3>
<ol>
<li>
<p>

 1. Start Anaconda Navigator, select environments on the left-hand bar, and click the triangle next to the environment you wish to run this program on and click “open Terminal”</p>
</li>
<li>
<p>
2. Type in the following code in terminal:</p>
<pre><code>

	    conda install -c conda-forge opencv
	    conda install -c conda-forge numpy
	    conda install -c conda-forge tensorflow
	    conda install -c conda-forge pillow
</code></pre>
</li>
<li>
<p>Clone <a href="3. Clone [League Minimap Scanner v 1.0.0](https://github.com/dcheng728/League-Minimap-Scanner/tree/master/League%20Minimap%20Scanner%20v%201.0.0" title= "League Minimap Scanner v 1.0.0">League Minimap Scanner v 1.0.0</a> from this repository, and run <a href="http://liveidentify.py">liveidentify.py</a> once you finished downloading.</p>
</li>
</ol>
<h2 id="overview">Overview</h2>
<p>) from this repository, and run liveidentify.py once you finished downloading.

## Overview

This Application aims to recognize League of Legends champions by examining the Minimap. The Algorithm takes an image of the minimap as input and returns the coordinates of enemy champions.</p>
<p>

The Algorithm is composed of 2 parts:</p>
<p>

1: Image Processing ( <a href="http://process.py">process.py</a> , <a href="http://live.py">live.py</a> )</p>
<p>2: Neural Network Evaluation ( <a href="http://image2numpy.py">image2numpy.py</a> , <a href="http://cnn.py">cnn.py</a> , <a href="http://evaluate.py">evaluate.py</a> )</p>



## Image Processing</h2>
<p>

The Image Processing component is responsible for preprocessing the minimap images before feeding it into the neural network. To reduce the computational cost of the neural network, the preprocessing  component will cut out the minimap regions where a champion icon’'s ring is detected using Opencv, whose process is as follows:

1. split 3-d image into b,g,r channels

2. use inRange function to binarize the b,g,r channels

3. deduct b and g from red channel to isolate the red channel (the color of enemy champions’' rings)

4. Run HoughCircles function to detect the red circles in red channel

5. Cut out squares based on coordinates of the circles and output them

After processing the image, the only inputs to the Neural Network are five 24*24 numpy arrays, which is much more computationally efficient compared to running object detection NN over the entire  minimap.</p>
<h2 id="neural-network">

## Neural Network</h2>
<p>

The neural network is trained on 31 champions with roughly 360 images each. The size of training images numpy is (19000+,24,24,3) and such for test images is (1000+,24,24,3). To collect the data, an AutoHotKey  script was written. Once initiated, the script would start a training game from the League of Legends  Client, select friendly champion and enemy champion and start the game with a python program constantly  grabbing the [805:1080,1645:1920] pixels of the monitor. Then the script will process the images itself  and cut out the champions’' portraits automatically.</p>
<p>

The advantage to this approach is a small training dataset size and fast training. The over 20,000<br>
images only took up 35MB of space when saved as “".npy”" files. Training the NN for 10 epochs took less  than 30 seconds on a gaming laptop.</p>
<p>

A weakness of the data collecting method is the deficiency of champions to choose from in League of Legends’' practicetool. To collect training samples of all champions, the screen-grabbing program would have to overlook actual games, and the champion portraits might need to be labeled manually. In future versions, this algorithm will learn to recognize more champions, and I will be able to justify playing  League of Legends as “"researching”" :)</p>
<p>

The training data are kept in /data/, train_images.npy (19000+,24,24,3), test_images.npy (1000+,24,24,3).</p>




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQxMjc5MzY5NCw1NTU4OTE2NjcsMTA5OT
EzMzMzOF19
-->