import React from 'react';


const Main = () => {
    return (
        <div id="page-content" className="index-page container">
	<div className="row">
		<div className="col-md-6 col-md-offset-1">
			<div id="main-content">
                {/* This will be used with a foreach */}
				{/* <article>
					<div className="art-header">
						<a href="single.html"><h2>Lorem ipsum dolor sit amet</h2></a>
						<div className="info">
							By <a href="#">Admin</a> June 12, 2015 - <i className="fa fa-comment"></i> 0 Comments
							<ul className="list-inline">
								<li><a href="#">Free</a></li>
								<li> - </li>
								<li>
									<span className="rating">
										<i className="fa fa-star"></i>
										<i className="fa fa-star"></i>
										<i className="fa fa-star"></i>
										<i className="fa fa-star"></i>
										<i className="fa fa-star-half-o"></i>
									</span>
								</li>
							</ul>
						</div>
					</div>
					<div className="art-content">
						<img src="../images/1.png" />
						<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor inviduntut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.justo duo dolores et ea rebum. Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt orem ipsum dolor sit amet, consetetur sadipscing <a href="single.html">MORE...</a></p>
					</div>
				</article>
			  <hr/> */}
				
				<center>
					<ul className="pagination">
						<li>
						  <a href="#" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						  </a>
						</li>
						<li><a href="#">1</a></li>
						<li><a href="#">2</a></li>
						<li><a href="#">3</a></li>
						<li><a href="#">4</a></li>
						<li><a href="#">5</a></li>
						<li>
						  <a href="#" aria-label="Next">
							<span aria-hidden="true">&raquo;</span>
						  </a>
						</li>
					</ul>
				</center>
		
			</div>
		</div>
		<div className="col-md-4">
			<div className="bs-sidebar affix hidden-xs hidden-sm" id="sidebar">
				<h3>Most Reviewed</h3>
				<div id="owl-demo1" className="owl-carousel">
					<div className="item">
						<a href="single.html"><img src="images/1.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/2.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/7.jpg" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/3.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/4.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/5.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/6.png" /></a>
					</div>
				</div>
				<h3>New Releases</h3>
				<div id="owl-demo2" className="owl-carousel">
					<div className="item">
						<a href="single.html"><img src="images/1.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/2.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/7.jpg" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/3.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/4.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/5.png" /></a>
					</div>
					<div className="item">
						<a href="single.html"><img src="images/6.png" /></a>
					</div>
				</div>
			</div>
		</div>
    </div>
	</div>
    );
};

export default Main;
