# Parcial 3 - PC

## Plataforma probada

Windows 11

## Resolución de pantalla usada

1920x1080

## Coordenadas manuales usadar para iniciar el llenado

El script detecta automaticamente la resolución de la pantalla y genera de manera porcentual la ubicación del cursor.

## Nombres de integrantes y contribuciones

| Matrícula | Nombre                        | Contribución                                      |
|-----------|-------------------------------|---------------------------------------------------|
| 2225457   | Julio Abraham Puente Guerrero | Logica principal, ejecución cruzada y repositorio |
| 2225388   | Sebastián Alighieri Ramírez   | Movimiento de cursor y manejo de errores          |
| 2153884   | Alberto Jessier Lucio Sital   | Logging y capturas de pantalla                    |

## Comando(s) de PowerShell ejecutados

```pwsh
Stop-Process -Name "msedge" -Force ; Start-Sleep -Seconds 1 ; Start-Process "msedge" -ArgumentList @("https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NURjFZQjdBMkJNSlkwQkVCM0c2V0cyWTVHNSQlQCNjPTEu&classId=31f16070-5361-4de8-9624-98f60a6f24ae&assignmentId=c865c317-1511-4faa-8a46-565ecf1dd392&submissionId=d6e96aee-73d5-bc05-1769-7e7db0c29f9d&route=shorturl", "--new-window", "--start-fullscreen")"
```
