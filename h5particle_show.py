#!/usr/bin/env python3

import h5py
import numpy as np


def show(item, root='/'):
	for name in item.attrs:
		print(f'{root}{name} Attribute: {item.attrs[name]}')

	for name in item.keys():
		cmp_name = f'{root}{name}/'
		if isinstance(item[cmp_name], h5py.Group):
			show(item[cmp_name], cmp_name)
		else:
			print(f'{root}{name} Data set: {item[name]}')


def particle_offset_factory(group):
	group.attrs['offset'] = np.random.random()
	group['value'] = np.random.random((1, 2))
	group.attrs['max'] = group.attrs['offset'] + group['value'][:].max()
	group.attrs['min'] = group.attrs['offset'] + group['value'][:].min()
	group.attrs['unitConversion'] = np.double(1)
	group.attrs['unitDescription'] = 'Some SI unit'
	group.attrs['unitSymbol'] = ''


def particle_map_factory(group, map_values):
	group['index'] = np.array([0, 1], dtype=np.uint8)
	group.attrs['valueMap'] = map_values


def particle_factory(group):
	group.attrs['charge'] = 200e-12
	group.attrs['NumberOfParticles'] = 2

	particle_offset_factory(group.create_group('x'))
	particle_offset_factory(group.create_group('px'))
	particle_offset_factory(group.create_group('y'))
	particle_offset_factory(group.create_group('py'))
	particle_offset_factory(group.create_group('t'))
	particle_offset_factory(group.create_group('pz'))
	particle_map_factory(group.create_group('status'), [b'Alive', b'InValid'])
	particle_offset_factory(group.create_group('charge'))
	particle_map_factory(group.create_group('species'), [b'electron', b'positron'])


def dump_factory(group):
	group.attrs['s'] = np.random.random()
	group.attrs['ElementDescription'] = 'Dump'
	group.attrs['ElementIndex'] = np.uint64(23)
	particle_factory(group.create_group('particle'))


def root_factory(file):
	file.attrs['README'] = 'This standard is cool'
	file.attrs['openPMD'] = '1.0.0'
	file.attrs['openPMDextension'] = np.uint32(1)
	file.attrs['software'] = 'hparticle_show.py V0.0.1'
	file.attrs['author'] = 'Marc Guetg marcg@slac.stanford.edu'
	file.attrs['date'] = '2017-10-30 23:59:59 -0800'
	file.attrs['timestamp'] = 0.0

	dump_factory(file.create_group('000000'))
	dump_factory(file.create_group('000001'))


if __name__ == '__main__':
	file = h5py.File('h5particle_show.h5', 'w')
	root_factory(file)
	show(file)
