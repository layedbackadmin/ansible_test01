- name: restart_dns
  service:
    name: "{{ dns_service }}"
    state: restarted
