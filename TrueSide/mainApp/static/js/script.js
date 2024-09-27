function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('sidebar__hidden');

    const sidebarHandler = document.getElementById('sidebar__handler');
    sidebarHandler.classList.toggle('clicked');
}