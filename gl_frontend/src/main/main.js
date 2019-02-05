import React from 'react';


const Main = () => {
    return (
        <div id="page-content" className="index-page container">
	<div className="row">
		<div className="col-md-6 col-md-offset-1">
			<div id="main-content">
				<article>
					<div className="art-header">
						<a href="single.html"><h2>Super Mario World</h2></a>
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
						<img src="https://images.igdb.com/igdb/image/upload/t_cover_big/co1hjg.jpg" />
						<button class="btn btn-primary btn-block mar-lg-bottom "/>
						<p>Super Mario World (known in Japan as Super Mario World: Super Mario Bros. 4) is a side-scrolling platformer developed by Nintendo EAD and published by Nintendo for the Super Nintendo Entertainment System on November 21, 1990 (in Japan), August 31, 1991 (in North America), and April 11, 1992 (in Europe). One of the launch titles of the SNES (and bundled with early systems in North America), Super Mario World is the fifth main game in the Super Mario series. (starring Nintendo's mascot, Mario, and his brother, Luigi). The game follows both Mario brothers as they explore Dinosaur Land (known for its large amount of dinosaurs) to find and defeat the evil Koopa king Bowser (and his seven underlings, the Koopalings) while rescuing Princess Toadstool. 
Along with new abilities (such as the "Spin Jump"), a new power-up (the "Cape Feather") and more obstacles, the game introduces dinosaur companions (known as Yoshi) that Mario and Luigi can ride. Yoshi, known for using their long tongues to snare and eat enemies, have become a fan-favorite among the series (giving them their own games and spin-offs, most notably this game's prequel). Special bundles of the SNES in 1994 included a compilation cartridge mixing Super Mario World with Super Mario All-Stars. The only difference in this version is a new sprite set for Luigi. The original game was later ported to the Game Boy Advance on February 11, 2002 as Super Mario World: Super Mario Advance 2. Along with a special version of the original Mario Bros., the port includes a variety of differences, including Luigi as a selectable character (who now has unique features, such as his floating jump from Super Mario Bros. 2), new voice acting, and the ability to save anywhere. The original game was also digitally re-released in Nintendo's Virtual Console platform for the Wii (on February 5, 2007) and Wii U (on April 26, 2013).<a href="single.html">MORE...</a></p>
					</div>
				</article>
			  <hr/>
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
