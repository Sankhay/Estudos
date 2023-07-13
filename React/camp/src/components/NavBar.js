import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';

export const NavBar = () => {
    return (
        <Navbar className={scrolled ? "scrolled": ""} expand='lg'>
            <Container>
                <Navbar.Brand href='#home'>React-Bootstrap</Navbar.Brand>
                    <img src={''} alt='Logo'/>
                <Navbar.Toggle aria-controls='basic-Navbar-nav' />
                    <span className='navbar-toggler-icon'></span>
                <Navbar.Collapse id='basic-Navbar-nav'>
                    <Nav className='me-auto'>
                        <Nav.Link href='#home' className={activeLink === 'home'}>Home</Nav.Link>
                        <Nav.Link href='#skills'>Skills</Nav.Link>
                        <Nav.Link href='#projects'>Projects</Nav.Link>
                    </Nav>
                    <span className='navbar-text'>
                        <div className='social-icon'>

                        </div>
                    </span>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

